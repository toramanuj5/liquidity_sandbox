# backend/haystack/haystack_pipeline.py
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import EmbeddingRetriever, PDFToTextConverter, PreProcessor
from haystack.pipelines import DocumentSearchPipeline
from haystack.utils import clean_wiki_text
import os

document_store = FAISSDocumentStore(embedding_dim=768, faiss_index_factory_str="Flat")

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-mpnet-base-v2",
    model_format="sentence_transformers"
)

document_store.update_embeddings(retriever)

rag_pipeline = DocumentSearchPipeline(retriever)
