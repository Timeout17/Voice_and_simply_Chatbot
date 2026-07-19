
from groq import Groq
from Project.src.Enums.llm_models import LLMmodels
from Project.src.Enums.Role import UserEnum

class AIAgentClass():

    def __init__(self, client: str):
        self.model = LLMmodels.GROQ_MODEL.value
        self.client = client

    def Answer(self, message: str):
        chat_completion = self.client.chat.completions.create(
            messages =[
                {
                "role": UserEnum.USER.value,
                "content": message
                }
            ],
            model = self.model
        )

        return chat_completion.choices[0].message.content
   