from fastapi import FastAPI
from models.schema import ChatRequest
from services.chatbot import ask_llm

app = FastAPI()

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    return {"reply": ask_llm(request.user_input)}