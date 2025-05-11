from core.embedding.manager import EmbeddingManager
from langchain_community.embeddings import HuggingFaceEmbeddings

class PersianEmbeddingManager(EmbeddingManager):
    """Responsible only for managing Persian embeddings"""
    
    def __init__(self, device: str = "cpu", embedding_model: str = "HooshvareLab/bert-fa-base-uncased"):
        self.device = device
        self.model_name = embedding_model
    
    def get_embeddings(self):
        """Get Persian embeddings model"""
        return HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={'device': self.device}
        )