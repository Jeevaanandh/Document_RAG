from fastapi import FastAPI, UploadFile, File, Request
import io
from dotenv import load_dotenv
from transformers import AutoModel, AutoTokenizer
import ollama
from mistralai import Mistral
import faiss
import torch
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import shutil
import os
from pydantic import BaseModel

class PromptRequest(BaseModel):
    query: str

load_dotenv()

app= FastAPI()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

texts=[]
faiss_index = None
all_chunks = []

model= AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
tokenizer= AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')


def getChunks(page,maxTokens= 256, stride= 128):
        words= page.split()
        chunks=[]
        i=0

        while(i< len(words)):
            chunk= " ".join(words[i:i+maxTokens])
            chunks.append(chunk)
            i+=stride

        return chunks

def getEmbeddings(text):
    with torch.no_grad():
        text_token= tokenizer(text, padding=True, truncation= True, return_tensors='pt')
        model_output= model(**text_token)
        embedding= model_output[0]
        attention_mask= text_token['attention_mask']
        input_mask_expanded= attention_mask.unsqueeze(-1).expand(embedding.size()).float()

        ## Returning the pooled 1D embedding
        return (torch.sum(embedding*input_mask_expanded,1)/torch.clamp(input_mask_expanded.sum(1), min= 1e-9)).squeeze(0)


@app.post("/upload")
async def OCR(file: UploadFile= File(...)):
    global faiss_index
    global all_chunks
    contents= await file.read()  ## The file is read as bytes

    
    client= Mistral(api_key=MISTRAL_API_KEY)


    upload_file= client.files.upload(
        file={
            "file_name": file.filename,
            "content": contents
        },
        purpose= "ocr"
    )

    signed_url= client.files.get_signed_url(file_id= upload_file.id)

    ocr_response= client.ocr.process(
        model= "mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": signed_url.url
        },
        include_image_base64= True
    )

    texts=[page.markdown for page in ocr_response.pages]

    
    
        
    embeddings=[]
    all_chunks.clear()
    

    for page in texts:
        chunks= getChunks(page)

        for chunk in chunks:
            emb= getEmbeddings(chunk)
            embeddings.append(emb)
            all_chunks.append(chunk)


    embedding_tensor= torch.stack(embeddings)
    embedding_array= embedding_tensor.detach().numpy().astype('float32')

    d= embedding_array.shape[1]

    faiss_index= faiss.IndexFlatL2(d)
    faiss_index.add(embedding_array)


    return JSONResponse(content={"message": "Success", "filename": file.filename})


@app.post("/prompt")
async def getAnswer(req: PromptRequest):

    query = req.query

    global faiss_index
    p_embedding= getEmbeddings(query).detach().numpy().astype('float32').reshape(1,-1)

    D,I= faiss_index.search(p_embedding, 5)

    relevant_chunks=[]

    for i in I[0]:
        relevant_chunks.append(all_chunks[i])
        


    client= ollama.Client()
    model= 'llama2'

    context= '\n\n'.join(relevant_chunks)

    prompt = f"""You are an assistant that answers based on a PDF document answer only based on the context always answer in third person.

    Context:
    {context}

    Question:
    {query}

    Answer:"""

    response= client.generate(model= model, prompt= prompt)


    return JSONResponse(content={"message": "Success", "answer":response.response})

