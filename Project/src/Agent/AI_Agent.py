
from Project.src.Enums.llm_models import LLMmodels
from Project.src.Agent.ContentCreation import ContentCreatonClass
from Project.src.Agent.LLMSercive import LLMServiceClass


class AIAgentClass():

    def __init__(self, client: str):
        self.model = LLMmodels.GROQ_MODEL.value
        self.client = client

    def Answer(self, message: str, history: list[str]):
        if self.client is None:
            return "Klines nem találhato"
        
        content: list[dict[str, str]] = ContentCreatonClass.create_message(history, message)

        response = LLMServiceClass.ChatService(                                  
            self.client, 
            content
            )
        
        ai_answer: str = response.choices[0].message.content

        return ai_answer