# tests/conftest.py
import pytest
from unittest.mock import MagicMock, patch

# Patch transformers.pipeline BEFORE importing day02
mock_pipeline = MagicMock()
mock_pipeline.return_value = {"answer": "dummy answer"}

patcher = patch("transformers.pipeline", return_value=mock_pipeline)
patcher.start()  # activates the patch

import day02  # now imports safely because pipeline is mocked

@pytest.fixture(autouse=True)
def stop_patch():
    yield
    patcher.stop()
