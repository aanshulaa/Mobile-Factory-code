from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_valid_order():
    response = client.post("/orders", json={"components": ["A", "D", "F", "I", "K"]})
    assert response.status_code == 201
    data = response.json()
    assert data["total"] == 142.3
    assert data["parts"] == ["LED Screen", "Wide-Angle Camera", "USB-C Port", "Android OS", "Metallic Body"]

def test_create_invalid_order():
    response = client.post("/orders", json={"components": ["A", "B", "D", "F", "I", "K"]})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid order configuration."}
