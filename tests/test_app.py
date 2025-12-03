# tests/test_app.py
from fastapi.testclient import TestClient
from day02 import app  # <--- import from your FastAPI file

client = TestClient(app)

def test_root():
    response = client.get("/chat")  # change to an endpoint that exists
    assert response.status_code == 405  # POST required, GET not allowed

def test_chat():
    payload = {
        "question": "What does Hugging Face provide?",
        "context": "Hugging Face is a technology company that provides open-source NLP libraries ..."
    }
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    assert "answer" in response.json()
