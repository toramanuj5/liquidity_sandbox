from fastapi import FastAPI
from backend.haystack import router as haystack_router

app = FastAPI()
app.include_router(haystack_router, prefix="/haystack")

