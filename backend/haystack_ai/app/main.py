# backend/haystack/app/main.py
from fastapi import FastAPI
from haystack_ai.haystack_router import router

app = FastAPI()
app.include_router(router)
