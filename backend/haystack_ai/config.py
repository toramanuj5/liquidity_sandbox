from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import SentenceTransformersDocumentEmbedder

def get_document_store():
    return InMemoryDocumentStore(use_bm25=True)

def get_embedder():
    return SentenceTransformersDocumentEmbedder(model_name_or_path="sentence-transformers/all-MiniLM-L6-v2")
