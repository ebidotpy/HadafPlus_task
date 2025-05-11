from abc import ABC, abstractmethod

class EmbeddingManager(ABC):
    """Abstract base class for embedding management"""
    
    @abstractmethod
    def get_embeddings(self):
        pass
