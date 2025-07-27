import React, {useState} from 'react'

function PromptView(props){
    const [prompt, setPrompt]= useState("");

    const [empty, setEmpty]= useState(true);

    const [response, setResponse]= useState("")

    const [messages, setMessages] = useState([]);


    function handleSubmit() {
        if (prompt !== "") {
            // Add user message
            setMessages(prev => [...prev, { sender: "user", text: prompt }]);
    

            fetch('http://localhost:8000/prompt', {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: prompt })
            })
            .then((response) => response.json())
            .then((data) => {
                // Add AI response
                setMessages(prev => [...prev, { sender: "ai", text: data.answer }]);
                
            });

            setPrompt(""); // Clear input field
        }
    }

    function handleBack(){
        props.setGoHome(false)
    }

    function handleChange(e){
        setPrompt(e.target.value)
    }



    return(
        <div className="app2">

            {empty && <h1 style={{fontFamily: 'monospace', color: 'white'}}>Ask questions...</h1>}

            <div className="chat-container">
                {messages.map((msg, index) => (
                    <div
                    key={index}
                    className={`chat-bubble ${msg.sender === 'user' ? 'user-bubble' : 'ai-bubble'}`}
                    >
                    {msg.text}
                    </div>
                ))}
            </div>

            <button onClick={handleBack} className='back-btn'>Back</button>


            <div className='footer'>
                <input type='text' className='text-bar' placeholder='Ask about document...' onChange={handleChange} value={prompt} ></input>
                <button className='submit-btn' onClick={handleSubmit}>Submit</button>

            </div>



            

            
        </div>
    )

}

export default PromptView