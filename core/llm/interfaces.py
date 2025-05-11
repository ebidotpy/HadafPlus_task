from abc import ABC, abstractmethod

class LLMInterface(ABC):
    """Abstract base class for LLM interfaces"""
    
    @abstractmethod
    def initialize(self):
        pass
