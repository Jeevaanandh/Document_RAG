# Retrieval-Augmented Generation (RAG) Application

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-yellow)
![MistralOCR](https://img.shields.io/badge/OCR-MistralOCR-orange)

A full-stack **Retrieval-Augmented Generation (RAG)** application designed to answer queries with **document retrieval + LLM generation**. It features **Mistral OCR** for document parsing, a **FastAPI backend**, and a **React-based frontend**, with **FAISS** powering semantic search.

---

## 📑 Table of Contents
1. [✨ Features](#-features)
2. [🔄 Pipeline](#-pipeline)
3. [⚙ Tech Stack](#-tech-stack)
4. [🛠 Backend Overview](#-backend-overview)
5. [🎨 Frontend Overview](#-frontend-overview)
6. [🌐 API Endpoints](#-api-endpoints)
7. [📸 Screenshots](#-screenshots)

---

## ✨ Features
- **Document OCR**: Extracts text and tables from PDFs using **Mistral OCR**.
- **Semantic Search**: Retrieves relevant chunks from documents using **FAISS vector store**.
- **LLM-powered Answers**: Uses **Llama 2** for context-aware responses.
- **Modern UI**: React chat interface with a futuristic dark theme.
- **RAG Pipeline**: Combines retrieval and generation seamlessly.
- **Lightweight & Fast**: Optimized backend with no heavy database dependency.




---

## 🔄 Pipeline
1. **Document Upload**: PDFs are parsed using **Mistral OCR** to extract text and tables.
2. **Embedding Generation**: Text chunks are embedded using `sentence-transformers`.
3. **Query Handling**: User queries are converted into embeddings.
4. **Vector Search**: FAISS retrieves top-k relevant chunks.
5. **Context Augmentation**: Retrieved content is fed to **Llama 2**.
6. **Response Generation**: Final response is returned to the frontend.

---

## ⚙ Tech Stack
| **Component**      | **Technology**            |
|--------------------|---------------------------|
| **Frontend**       | React,  CSS               |
| **Backend**        | FastAPI, Python 3.10      |
| **OCR**            | Mistral OCR               |
| **Vector Store**   | FAISS                     |
| **LLM**            | Llama 2 (Hugging Face)    |
| **Embeddings**     | Sentence Transformers     |





---

## 🛠 Backend Overview
- **FastAPI Routes**:
  - `/query` – Handles RAG pipeline queries.
  - `/upload` – Runs **Mistral OCR** to extract content from PDFs and stores embeddings.
  

- **Core Components**:
  - **Mistral OCR**: Text and table extraction from documents.
  - **FAISS**: Vector similarity search.
  - **LLM**: Generates answers from retrieved context.

---

## 🎨 Frontend Overview
- Built with **React + CSS**.
- **Chat-style interface** for smooth interaction.
- **Elegant scrollbars and dark theme** for a modern feel.
- Real-time response display.

---

## 🌐 API Endpoints
### **POST** `/upload`
### **POST** `/query`


---

## 📸 Screenshots


