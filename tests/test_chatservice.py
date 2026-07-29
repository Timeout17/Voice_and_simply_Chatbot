class FakeAgent:

    def Answer(self, prompt, memory):
        return "Teszt válasz"

    def Transcribe_audio(self, path):
        return "Tesztelt hang"


class FakeDAO:

    def save_message(self, message):
        return True

    def get_all_messages(self):
        return []

    def get_message_count(self):
        return 0

from Project.src.Logic.ChatService import ChatServiceClass


def test_answer_message():

    dao = FakeDAO()

    chat = ChatServiceClass(dao)

    chat.agent = FakeAgent()

    result = chat.Answer_message("Szia")

    assert result == "Teszt válasz"