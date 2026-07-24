from Project.src.models.Message import MessageClass
from Project.src.Adapters.LLMAdepters.GroqAdapter import GroqAdaptetClass
from Project.src.Agent.AI_Agent import AIAgentClass
from Project.src.Enums.Role import UserEnum
from Project.src.Adapters.VoiceAdapters.GttsAdapter import GTTSAdapterClass
from Project.src.Agent.SummaryMemory import SummaryServiceClass

class ChatServiceClass:

    def __init__(self, dao):

        self.userdao = dao

        groq_adapter = GroqAdaptetClass()
        self.agent = AIAgentClass(groq_adapter.client)

        self.voice = GTTSAdapterClass()
        self.summaryclass = SummaryServiceClass(self.agent)
        
    def _process_and_answer(self, prompt_text: str) -> str:
        """Belső segédfüggvény a közös logika kezelésére (DRY elv)."""
        # 1. Üzenet objektum létrehozása
        message_obj = MessageClass(
            prompt=prompt_text,
            role=UserEnum.USER.value
        )

        # 2. Mentés az adatbázisba
        if not self.userdao.save_message(message_obj):
            return "Nem menti el"

        # 3. Előzmények lekérése és formázása
        history = self.userdao.get_all_messages()
        memory = [
            {
                "role": m.role,
                "content": m.prompt
            }
            for m in history
        ]

        if (self.userdao.get_message_count() > 10):
            
            summary = self.summaryclass.create_summary(memory)

            message_obj = MessageClass(
            prompt=summary,
            role=UserEnum.SUMMARY.value
            )

            self.userdao.clear_messages_and_set_summary(message_obj)

            memory = [
                {
                    "role": UserEnum.SUMMARY.value,
                    "content": summary
                }
            ]
        # 4. Válasz generálása az LLM segítségével
        # Fontos: A prompt_text-et adjuk át, hangüzenet esetén is a transzkripciót!
        return self.agent.Answer(prompt_text, memory)

    def Answer_message(self, message: str) -> str:
        """Szöveges üzenet feldolgozása."""
        return self._process_and_answer(message)
            
    def Answer_voice_message(self, audio_file_path: str):

        transcribed_message = self.agent.Transcribe_audio(audio_file_path)

        answer = self._process_and_answer(transcribed_message)

        audio_path = self.voice.text_to_speech(
            answer,
            "response.mp3"
        )

        return answer, audio_path
