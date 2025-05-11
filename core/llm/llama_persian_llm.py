from core.llm.interfaces import LLMInterface
from langchain_community.llms import Ollama

class PersianLlamaInterface(LLMInterface):
    """Responsible only for communicating with Llama 3"""
    
    def __init__(self):
        self.llm = None
    
    def initialize(self):
        """Initialize Llama 3.2 model"""
        self.llm = Ollama(
            model="llama3.2",
            temperature=0.7,
            top_p=0.9,
            repeat_penalty=1.1,
            num_ctx=4096
        )
        if not self.llm:
            raise ValueError("Failed to initialize Llama 3 model")
        return self.llm
    
