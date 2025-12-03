# tests/test_app.py
from fastapi.testclient import TestClient
from main import app  # replace with your FastAPI app import

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.text or "FastAPI" in response.text
