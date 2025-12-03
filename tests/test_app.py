# tests/test_app.py
from fastapi.testclient import TestClient
from day02 import app  # now imports fine because pipeline is mocked

client = TestClient(app)

def test_chat():
    payload = {
        "question": "What does Hugging Face provide?",
        "context": "Hugging Face is a technology company that provides open-source NLP libraries ..."
    }
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    assert response.json()["answer"] == "dummy answer"
