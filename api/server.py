from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.rag import router as rag_router

def create_app():
    app = FastAPI(
        title="Persian RAG API",
        description="API for Persian Retrieval-Augmented Generation System",
        version="0.1.0"
    )
    
    # Setup CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    app.include_router(rag_router)
    
    return app

app = create_app()