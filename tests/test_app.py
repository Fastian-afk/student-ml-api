from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "wrong"
    assert data["application"] == "student-ml-api"
    assert data["version"] == "1.0.0"


def test_predict_success():
    response = client.post("/predict", json={"value": 10})

    assert response.status_code == 200

    data = response.json()

    assert data["input"] == 10
    assert data["prediction"] == 20


def test_predict_missing_input():
    response = client.post("/predict", json={})

    assert response.status_code == 422


def test_predict_invalid_input():
    response = client.post("/predict", json={"value": "not-a-number"})

    assert response.status_code == 422