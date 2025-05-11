from fastapi import APIRouter, Depends
from api.models import QueryRequest, QueryResponse
from core.rag.system import PersianRAGSystem
from api.dependencies import get_rag_system
import time

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
    
    return QueryResponse(
        answer=answer,
        processing_time=time.time() - start_time
    )