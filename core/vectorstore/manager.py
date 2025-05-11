from typing import List
import os
from langchain.schema import Document
from langchain_community.vectorstores import FAISS

class VectorStoreManager:
    """Responsible only for managing the vector store"""
    
    def __init__(self, embeddings, persist_dir: str = "/home/ebi/machinelearning/HadafPlus_task/data/processed/faiss_index"):
        self.embeddings = embeddings
        self.persist_dir = persist_dir
        self.vectorstore = None
    
    def create_store(self, documents: List[Document]):
        """Create or load vector store"""
        if os.path.exists(self.persist_dir):
            self.vectorstore = FAISS.load_local(
                self.persist_dir, 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )
        else:
            self.vectorstore = FAISS.from_documents(documents, self.embeddings)
            self.vectorstore.save_local(self.persist_dir)
        return self.vectorstore.as_retriever(search_kwargs={"k": 3})