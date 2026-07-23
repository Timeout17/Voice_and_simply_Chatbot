from Project.src.Enums.llm_models import LLMmodels

class LLMServiceClass():
    @staticmethod
    def ChatService(client: str, content: str):
            response = client.chat.completions.create(
                model = LLMmodels.GROQ_MODEL.value,
                messages = content,
                temperature = 0.5,
                max_completion_tokens = 1024,
            )

            return response