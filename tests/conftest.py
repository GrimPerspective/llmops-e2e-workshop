# tests/conftest.py
import pytest
from unittest.mock import MagicMock
import day02

@pytest.fixture(autouse=True)
def mock_pipeline(monkeypatch):
    # Create a dummy pipeline that returns a fixed answer
    dummy_pipeline = MagicMock()
    dummy_pipeline.return_value = {"answer": "dummy answer"}
    monkeypatch.setattr(day02, "qa_pipeline", dummy_pipeline)
