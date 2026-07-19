from Project.src.Adapters.LLMAdepters.MainAdapter import MainAdapter
import os
from groq import Groq

class GroqAdaptetClass(MainAdapter):
    
    def __init__(self):
        self.api_key = os.environ.get("GROQ_API_KEY")
        self.client = None

        self.create_client()
        
    def create_client(self) -> Groq:
        if self.api_key:
            self.client = Groq(api_key=self.api_key)
            # ide egy loggingot
        else:
            pass
            # a mások log
            
        return self.client