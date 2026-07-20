import os
from Project.src.Adapters.LLMAdepters.MainAdapter import MainAdapter
from huggingface_hub import InferenceClient

class HuggingfaceAdapterClass(MainAdapter):
    
    def __init__(self):
        self.api_key = os.environ.get("HF_TOKEN")
        self.model = "meta-llama/Llama-3.2-3B-Instruct"
        
        self.client = None


        self.create_client()
    def create_client(self):
        if self.api_key:
            self.client = InferenceClient(model=self.model, token=self.api_key)
            # ide is loggolunk

        else:
            pass
            # ide is loggolunk