from typing import List
import os
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document

class DocumentLoader:
    """Responsible only for loading documents from a directory"""
    
    def __init__(self, directory: str):
        self.directory = directory
    
    def load_pdfs(self) -> List[Document]:
        """Load all PDF documents from the directory"""
        documents = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".pdf"):
                filepath = os.path.join(self.directory, filename)
                try:
                    loader = PyPDFLoader(filepath)
                    documents.extend(loader.load())
                except Exception as e:
                    print(f"Error loading {filename}: {str(e)}")
                    continue
        return documents