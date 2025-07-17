from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory vector store
index = faiss.IndexFlatL2(384)
doc_chunks = []

def ingest_document(doc_text: str):
    global doc_chunks
    chunks = [doc_text[i:i+500] for i in range(0, len(doc_text), 500)]
    vectors = model.encode(chunks)
    index.add(np.array(vectors).astype("float32"))
    doc_chunks = chunks

def query_document(question: str) -> str:
    q_vector = model.encode([question]).astype("float32")
    D, I = index.search(q_vector, k=3)
    results = [doc_chunks[i] for i in I[0]]
    return "\n---\n".join(results)
