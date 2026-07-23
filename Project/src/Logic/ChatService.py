from Project.src.models.Message import MessageClass
from Project.src.Adapters.LLMAdepters.GroqAdapter import GroqAdaptetClass
from Project.src.Agent.AI_Agent import AIAgentClass
from Project.src.Enums.Role import UserEnum
from Project.src.data.DAO import MessageDAOClass
from Project.src.data.DataBaseConnention import DataBaseConnentionClass


class ChatServiceCLass():
    def __init__(self, dao):
        # a jövőbeli DAO-nak
        self.userdao = dao
        

    def Answer_message(self, message: str):

        # el küldi megnéztni, hogy minden jó-e
        # utána ellenőriz, hogy külhet-e még üzentett a felhasználó

        # ha igen, akkor objektumosítja, és küldi tovább a DAO-nak

        text: MessageClass = MessageClass(
            prompt=message,
            role=UserEnum.USER.value
        )

        if (self.userdao.save_message(text)):

            history = self.userdao.get_all_messages()

            memory = [
                        {
                            "role": m.role,
                            "content": m.prompt
                        }
                        for m in history
                    ]

            groq_adapter = GroqAdaptetClass()
            client = groq_adapter.client

            Agent = AIAgentClass(client)
            
            result = Agent.Answer(message, memory)


            return result
        return "Nem menti el"
            
        