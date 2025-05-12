import torch
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from core.document_processing.loader import DocumentLoader
from core.document_processing.splitter import PersianTextSplitter
from core.vectorstore.manager import VectorStoreManager
from core.embedding.persian_embedding_manager import PersianEmbeddingManager
from core.llm.llama_persian_llm import PersianLlamaInterface
from core.prompt_structure.prompts_manager import PromptEngineer
from config.settings import settings

class PersianRAGSystem:
    """Orchestrates all components while maintaining SRP"""
    
    def __init__(self, pdf_dir: str = "/home/ebi/machinelearning/HadafPlus_task/data/input"):
        self.pdf_dir = pdf_dir
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.retriever = None
        self.chain = None
        
        # Initialize components
        self.document_loader = DocumentLoader(pdf_dir)
        self.text_splitter = PersianTextSplitter(
            chunk_size=settings.CHUNK_SIZE, 
            chunk_overlap=settings.CHUNK_OVERLAP
        )
        self.embedding_manager = PersianEmbeddingManager(
            device=self.device, 
            embedding_model=settings.EMBEDDING_MODEL
        )
        self.llm_interface = PersianLlamaInterface(
            model=settings.LLM_MODEL, 
            temprature=settings.LLM_TEMPERATURE
        )
        self.prompt_engineer = PromptEngineer()
    
    def initialize(self):
        """Initialize all components"""
        print("Initializing Persian RAG system...")
        
        # Document processing pipeline
        documents = self.document_loader.load_pdfs()
        split_docs = self.text_splitter.split_documents(documents)
        
        # Vector store pipeline
        embeddings = self.embedding_manager.get_embeddings()
        vector_store = VectorStoreManager(
            embeddings=embeddings, 
            persist_dir=settings.VECTOR_STORE_PATH
        )
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
        
    def get_retrieved_documents(self, question: str, k: int = 3) -> list:
      """Directly access retrieved documents"""
      return self.retriever.get_relevant_documents(question, k=k)