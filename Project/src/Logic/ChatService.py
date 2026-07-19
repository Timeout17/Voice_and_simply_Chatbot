from Project.src.models.Message import MessageClass
from Project.src.Adapters.LLMAdepters.GroqAdapter import GroqAdaptetClass
from Project.src.Agent.AI_Agent import AIAgentClass
from Project.src.Enums.Role import UserEnum


class ChatServiceCLass():
    def __int__(self):
        # a jövőbeli DAO-nak
        pass

    def Answer_message(self, message: str):

        # el küldi megnéztni, hogy minden jó-e
        # utána ellenőriz, hogy külhet-e még üzentett a felhasználó

        # ha igen, akkor objektumosítja, és küldi tovább a DAO-nak

        text: MessageClass = MessageClass(
            prompt=message,
            role=UserEnum.USER.value
        )

        # vissza, jön, hogy mentette, ha igen, akkor adja tovább

        # jön egy rútert ami dönt, hogy akkor az üzenet hossza alapján, melyik model legyen használva
        # most Groq ai csak
        # Adaptert meghívjuk

        groq_adapter = GroqAdaptetClass()
        client = groq_adapter.client

        Agent = AIAgentClass(client)

        return Agent.Answer(text.prompt)

        

        