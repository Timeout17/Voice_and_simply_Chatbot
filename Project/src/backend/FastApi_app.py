import os
import sys

# 1. Kiszámoljuk a legkülső gyökérmappát (C:\Chatbot) a jelenlegi fájlhoz képest
# FastApi_app.py (backend) -> src -> Project -> Chatbot (3 szintet lépünk vissza)
current_dir = os.path.dirname(os.path.abspath(__file__))
chatbot_root = os.path.abspath(os.path.join(current_dir, "../../.."))

# 2. Betesszük a legelső helyre a keresőben, így a "Project" mappa azonnal látható lesz
if chatbot_root not in sys.path:
    sys.path.insert(0, chatbot_root)

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from pathlib import Path
import uvicorn
import shutil
from Project.src.data.DataBaseConnention import DataBaseConnentionClass
from Project.src.data.DAO import MessageDAOClass
from Project.src.data.DatabaseInitializer import DatabaseInitializerClass
from Project.src.Logic.ChatService import ChatServiceClass



app = FastAPI(title="Simply bot")

class Message(BaseModel):
    prompt: str

@app.post("/query/voice")    
async def send_message(file: UploadFile = File(...)):

    try:
        audiofiles = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent / "audiofiles"
        audiofiles.mkdir(parents=True, exist_ok=True)

        file_path = audiofiles / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)


        conn = DataBaseConnentionClass().get_connection()
        userdao = MessageDAOClass(conn)

        chat = ChatServiceClass(userdao)

        answer, audio_path = chat.Answer_voice_message(str(file_path))

        return {
            "answer": answer,
            "audio_path": audio_path
        }

    except Exception as e:
        print("HIBA:", e)
        return {
            "error": str(e)
        }



@app.on_event("startup")
def CreateDatabase():
    conn = DataBaseConnentionClass()
    connection = conn.get_connection()

    initializer = DatabaseInitializerClass(connection)

    initializer.CreateMessagetable()

    connection.close()


@app.post("/query")
async def send_message(data: Message):
    
    # itt magát az üzenetet fogjuk majd messageclassba tenni, a könyebb kezelhetősség szempontjából
    
    ## amit úgy teszünk, hogy az chatServicet meghívjuk, aki majd kezeli ezt mint orkhesztrátor
    ## amit kapunk egy message objektum, amit már kezelt a többi osztály
    
    
    # megkapja az Agent, amire majd válaszol, és a választ oda adja az orhesztrátornek, aki majd összerakja üzenetté  

    conn = DataBaseConnentionClass().get_connection()

    userdao = MessageDAOClass(conn)
    
    chat: ChatServiceClass = ChatServiceClass(userdao)

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