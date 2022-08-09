from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

## get("/")


def test_get_all_registries():
    response = client.get("/")
    assert response.status_code == 200


## get("/id")


def test_get_registry_no_exist():
    response = client.get("/1")
    assert response.status_code == 404
