from fastapi import APIRouter, UploadFile
import pandas as pd
from .document_loader import load_documents_from_directory
from .haystack_pipeline import build_pipeline

router = APIRouter()
pipeline, document_store = build_pipeline()

@router.post("/upload-policy")
def upload_policy():
    docs = load_documents_from_directory("data/bank_policies")
    document_store.write_documents(docs)
    return {"message": f"{len(docs)} documents uploaded."}

@router.get("/gap-analysis")
def get_gap_analysis():
    gaps = [
        {"Rule": "Liquidity Buffers", "Found": False},
        {"Rule": "Stress Test Horizon", "Found": True},
        {"Rule": "Currency Mismatch", "Found": False}
    ]
    df = pd.DataFrame(gaps)
    csv_path = "data/compliance_gap_output.csv"
    df.to_csv(csv_path, index=False)
    return {"message": "Compliance Gap Report Generated", "file": csv_path}
