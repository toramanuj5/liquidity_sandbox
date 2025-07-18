from fastapi import FastAPI
from backend.haystack import haystack_router as haystack_router

app = FastAPI()
app.include_router(haystack_router, prefix="/haystack")

