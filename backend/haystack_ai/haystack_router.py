# backend/haystack/haystack_router.py
from fastapi import APIRouter, UploadFile
from haystack_ai.haystack_pipeline import document_store, retriever, rag_pipeline
from haystack_ai.document_loader import load_documents_from_directory

router = APIRouter()

@router.post("/upload/")
async def upload_docs():
    docs = load_documents_from_directory("data/bank_policies")
    document_store.write_documents(docs)
    document_store.update_embeddings(retriever)
    return {"status": "Documents indexed successfully"}

@router.get("/query/")
async def query_qa(q: str):
    result = rag_pipeline.run(query=q, params={"Retriever": {"top_k": 3}})
    return {"answers": result}
