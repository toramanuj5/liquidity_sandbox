"""from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os
from .utils import process_pdf_and_generate_compliance_gap

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    gap_file_path = process_pdf_and_generate_compliance_gap(file_path)
    return FileResponse(path=gap_file_path, filename="compliance_gap.xlsx", media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hello from Haystack"}

