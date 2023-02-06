import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture()
def client():
    """Client for API testing"""
    client = TestClient(app)
    return client