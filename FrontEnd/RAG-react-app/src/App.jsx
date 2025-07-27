import React, {useState} from 'react'
import PromptView from './PromptView';
import UploadPage from './UploadPage';

function App(){
  const [uploaded, setUploaded]= useState(false)
  return(
        <>

          <UploadPage upDone={uploaded} setupDone={setUploaded}></UploadPage>


          {uploaded && (
            <div className="prompt-overlay">
              <PromptView gohome={uploaded} setGoHome={setUploaded}></PromptView>
            </div>
          )}
              
        
        </> 

  )

}


export default App