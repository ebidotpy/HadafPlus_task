import torch
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from core.document_processing.loader import DocumentLoader
from core.document_processing.splitter import PersianTextSplitter
from core.vectorstore.manager import VectorStoreManager
from core.embedding.persian_embedding_manager import PersianEmbeddingManager
from core.llm.llama_persian_llm import PersianLlamaInterface
from core.prompt_structure.prompts_manager import PromptEngineer

class PersianRAGSystem:
    """Orchestrates all components while maintaining SRP"""
    
    def __init__(self, pdf_dir: str = "/home/ebi/machinelearning/HadafPlus_task/data/input"):
        self.pdf_dir = pdf_dir
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.retriever = None
        self.chain = None
        
        # Initialize components
        self.document_loader = DocumentLoader(pdf_dir)
        self.text_splitter = PersianTextSplitter()
        self.embedding_manager = PersianEmbeddingManager(self.device)
        self.llm_interface = PersianLlamaInterface()
        self.prompt_engineer = PromptEngineer()
    
    def initialize(self):
        """Initialize all components"""
        print("Initializing Persian RAG system...")
        
        # Document processing pipeline
        documents = self.document_loader.load_pdfs()
        split_docs = self.text_splitter.split_documents(documents)
        
        # Vector store pipeline
        embeddings = self.embedding_manager.get_embeddings()
        vector_store = VectorStoreManager(embeddings)
        self.retriever = vector_store.create_store(split_docs)
        
        # LLM pipeline
        llm = self.llm_interface.initialize()
        
        # Chain assembly
        prompt = self.prompt_engineer.get_rag_prompt()
        self.chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        
        print("System initialized successfully")
    
    def query(self, question: str) -> str:
        """Execute a query against the RAG system"""
        if not self.chain:
            raise ValueError("System not initialized")
        
        try:
            # Add Persian instruction to ensure Persian response
            formatted_question = f"{question} (پاسخ را به فارسی ارائه دهید)"
            return self.chain.invoke(formatted_question)
        except Exception as e:
            return f"Error processing query: {str(e)}"