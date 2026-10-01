from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import ask
from memory import load_memory, clear_memory

app = FastAPI(title="Easy LLM Chatbot")


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Easy LLM Chatbot API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    return ask(request.question)


@app.get("/memory")
def memory():
    return {"messages": load_memory()}


@app.delete("/memory")
def delete_memory():
    clear_memory()
    return {"message": "Conversation memory cleared"}
