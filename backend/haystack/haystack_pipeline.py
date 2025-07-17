from haystack.pipelines import DocumentSearchPipeline
from .config import get_document_store, get_embedder

def build_pipeline():
    document_store = get_document_store()
    retriever = get_embedder()
    pipeline = DocumentSearchPipeline(retriever)
    return pipeline, document_store
