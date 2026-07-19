from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

import os
import sys

app = FastAPI(title="Simply bot")

class Message(BaseModel):
    prompt: str


@app.post("/query")
def send_message(data: Message):
    
    # itt magát az üzenetet fogjuk majd messageclassba tenni, a könyebb kezelhetősség szempontjából
    
    ## amit úgy teszünk, hogy az chatServicet meghívjuk, aki majd kezeli ezt mint orkhesztrátor
    ## amit kapunk egy message objektum, amit már kezelt a többi osztály
    
    
    # megkapja az Agent, amire majd válaszol, és a választ oda adja az orhesztrátornek, aki majd összerakja üzenetté  
    
    return {"status": Message.prompt}


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__)) # ez a backend mappa
    project_root = os.path.abspath(os.path.join(current_dir, "../..")) # ez a Project mappa
    
    sys.path.append(project_root)
    
    uvicorn.run("src.backend.FastApi_app:app", host="127.0.0.1", port=8000, reload=True)
