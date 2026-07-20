from Project.src.Adapters.LLMAdepters.MainAdapter import MainAdapter
import os
from google import genai

class GroqAdaptetClass(MainAdapter):
    
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.client = None

        self.create_client()
        
    def create_client(self):
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
            # ide egy loggingot
        else:
            pass
            # a mások log
            
        return self.client