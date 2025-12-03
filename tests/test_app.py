# day02.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
qa_pipeline = None  # placeholder

class ChatRequest(BaseModel):
    question: str
    context: str

class ChatResponse(BaseModel):
    answer: str

@app.on_event("startup")
async def load_pipeline():
    global qa_pipeline
    from transformers import pipeline  # imported only when app starts
    qa_pipeline = pipeline(
        "question-answering",
        model="distilbert-base-uncased-distilled-squad"
    )

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        result = qa_pipeline(question=request.question, context=request.context)
        return ChatResponse(answer=result["answer"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
