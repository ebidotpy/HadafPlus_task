class Settings:
    # Document processing
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # Embeddings
    EMBEDDING_MODEL = "HooshvareLab/bert-fa-base-uncased"
    
    # Vector Store
    VECTOR_STORE_PATH = "/home/ebi/machinelearning/HadafPlus_task/data/processed/faiss_index"
    
    # LLM
    LLM_MODEL = "llama3.2"
    LLM_TEMPERATURE = 0.7

settings = Settings()