import React, {useState} from 'react'

function UploadPage(props){

    const [file, setFile]= useState(null);
    const [isLoading, setIsLoading] = useState(false);

    

    function handleFileInput(e){
        const selectedFile= e.target.files[0];
        setFile(selectedFile)

    }


    function handleUpload(){
        setIsLoading(true);
        const formData = new FormData();
        formData.append("file", file);

        fetch('http://localhost:8000/upload',{
        method:"POST",
        body: formData
        })
        .then((response) => response.json())
        .then((data) => {
        console.log("Upload Successful: ", data)
        setIsLoading(false);
        props.setupDone(true)
        })

    }

    return(
        <div className='app'>
        <h1 className='title'>Choose a file to get started...</h1>

        <div className='image_upload_div'>

            <input
            id= "fileInput"
            type= "file"
            accept= ".pdf, .doc, .docx, image/*"
            onChange= {handleFileInput}
            style= {{display: 'none'}}
            />

            <label htmlFor="fileInput" className="custom-file-upload">
                Choose File
            </label>

            {file && <h3>Selected File: {file.name}</h3>}

        </div>

        {file && <button 
            className='upload_btn' 
            onClick={handleUpload} 
            disabled={isLoading}
            >
            {isLoading ? (
                <>
                <span className="spinner"></span> Uploading...
                </>
            ) : "Upload"}
            </button>}

        </div>
    )




}


export default UploadPage