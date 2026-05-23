from fastapi import FastAPI
from routes.chat import chat_router

app = FastAPI(title="Taph AI")

app.include_router(chat_router, prefix="/chat")

@app.get("/")
def root():
    return {"message": "Welcome to Taph AI"}
