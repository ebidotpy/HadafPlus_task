from fastapi import APIRouter, Depends
from api.models import QueryRequest, QueryResponse
from core.rag.system import PersianRAGSystem
from api.dependencies import get_rag_system
import time
from helper.manage_retrieved_documents import show_retrieved_docs


router = APIRouter(prefix="/rag", tags=["RAG"])

@router.post("/query", response_model=QueryResponse)
async def query_rag(
    request: QueryRequest,
    rag_system: PersianRAGSystem = Depends(get_rag_system)
):
    start_time = time.time()
    
    answer = rag_system.query(
        question=request.question
    )
    docs = rag_system.get_retrieved_documents(request.question)
    
    return QueryResponse(
        question=request.question,
        answer=answer,
        sources=show_retrieved_docs(docs),
        processing_time=time.time() - start_time
    )