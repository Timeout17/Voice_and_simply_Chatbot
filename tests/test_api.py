from Project.src.backend.FastApi_app import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_query():

    response = client.post(
        "/query",
        json={"prompt": "Szia"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "status" in data