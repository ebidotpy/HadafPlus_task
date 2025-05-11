from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
class PersianTextSplitter:
    """Responsible only for splitting Persian text"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", "۔", "؟", "!", " ", ""]
        )
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks"""
        return self.splitter.split_documents(documents)