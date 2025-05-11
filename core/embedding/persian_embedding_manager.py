from core.embedding.manager import EmbeddingManager
from langchain_community.embeddings import HuggingFaceEmbeddings

class PersianEmbeddingManager(EmbeddingManager):
    """Responsible only for managing Persian embeddings"""
    
    def __init__(self, device: str = "cpu"):
        self.device = device
        self.model_name = "HooshvareLab/bert-fa-base-uncased"
    
    def get_embeddings(self):
        """Get Persian embeddings model"""
        return HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={'device': self.device}
        )