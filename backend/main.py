# backend/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from haystack_ai.haystack_router import query_qa, run_gap_analysis
from fastapi.middleware.cors import CORSMiddleware
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "haystack"))

from haystack_ai.haystack_router import query_qa, run_gap_analysis

app = FastAPI(
    title="Liquidity Risk Sandbox - Agentic AI Backend",
    description="Unified gateway for Haystack (QA + Gap Analysis)",
    version="1.0"
)

# Enable CORS for Streamlit frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "running", "modules": ["Haystack QA", "Gap Analysis"]}

@app.get("/qa/")
async def ask_question(q: str):
    """
    Ask a question based on ingested PDF documents
    """
    return query_qa(q)

@app.post("/gap-analysis/")
async def gap_analysis(file: UploadFile = File(...)):
    """
    Upload a PDF policy document and run compliance gap analysis
    """
    try:
        contents = await file.read()
        return run_gap_analysis(contents, file.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
