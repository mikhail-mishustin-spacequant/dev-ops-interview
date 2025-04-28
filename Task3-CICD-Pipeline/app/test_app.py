import pytest
import json
from app import app as flask_app

@pytest.fixture
def app():
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_endpoint(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "message" in data
    assert "version" in data
    assert data["status"] == "running"

def test_health_endpoint(client):
    response = client.get('/health')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "healthy"

def test_api_data_endpoint(client):
    response = client.get('/api/data')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "items" in data
    assert len(data["items"]) > 0
    assert "id" in data["items"][0]
    assert "name" in data["items"][0]
