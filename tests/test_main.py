from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "CI Pipeline Practice Started"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_user():
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json()["user_id"] == 1