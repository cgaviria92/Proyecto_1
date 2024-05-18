import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def auth_token():
    response = client.post(
        "/api/v1/auth/token",
        data={"username": "admin", "password": "admin"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    return token

def test_read_main(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_comprador(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/api/v1/users/comprador",
        json={"nombre": "Juan", "apellido": "Perez", "ciudad": "Bogotá", "direccion": "Tv. 70 #65b-75"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "Juan"

def test_create_vendedor(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/api/v1/users/vendedor",
        json={"nombre": "Ana", "apellido": "Lopez", "ciudad": "Medellin", "cargo": "asesor"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "Ana"
