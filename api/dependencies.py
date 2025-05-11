from fastapi import Depends
from core.rag.system import PersianRAGSystem

def get_rag_system():
    system = PersianRAGSystem()
    system.initialize()
    return system
