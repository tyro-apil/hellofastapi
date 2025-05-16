from fastapi.testclient import TestClient
from fast_api import app

client = TestClient(app)


def test_calculate_endpoint():
    response = client.post("/calculate", json={"operation": "add", "x": 5, "y": 3})
    assert response.status_code == 200
    assert response.json() == 8
