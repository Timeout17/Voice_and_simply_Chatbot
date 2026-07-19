import os
import sys

# 1. Kiszámoljuk a legkülső gyökérmappát (C:\Chatbot) a jelenlegi fájlhoz képest
# FastApi_app.py (backend) -> src -> Project -> Chatbot (3 szintet lépünk vissza)
current_dir = os.path.dirname(os.path.abspath(__file__))
chatbot_root = os.path.abspath(os.path.join(current_dir, "../../.."))

# 2. Betesszük a legelső helyre a keresőben, így a "Project" mappa azonnal látható lesz
if chatbot_root not in sys.path:
    sys.path.insert(0, chatbot_root)

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from Project.src.Logic.ChatService import ChatServiceCLass

app = FastAPI(title="Simply bot")

class Message(BaseModel):
    prompt: str


@app.post("/query")
def send_message(data: Message):
    
    # itt magát az üzenetet fogjuk majd messageclassba tenni, a könyebb kezelhetősség szempontjából
    
    ## amit úgy teszünk, hogy az chatServicet meghívjuk, aki majd kezeli ezt mint orkhesztrátor
    ## amit kapunk egy message objektum, amit már kezelt a többi osztály
    
    
    # megkapja az Agent, amire majd válaszol, és a választ oda adja az orhesztrátornek, aki majd összerakja üzenetté  
    
    chat:ChatServiceCLass = ChatServiceCLass()

    message = chat.Answer_message(data.prompt)

    return {"status": message}

if __name__ == "__main__":
    uvicorn.run(
        "Project.src.backend.FastApi_app:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        app_dir=chatbot_root
    )