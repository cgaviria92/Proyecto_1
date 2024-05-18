# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

# def test_create_comprador():
#     response = client.post(
#         "/api/v1/users/comprador",
#         json={"nombre": "Juan", "apellido": "Perez", "ciudad": "Bogota", "direccion": "Calle 123"}
#     )
#     assert response.status_code == 200
#     assert response.json()["nombre"] == "Juan"

# def test_create_vendedor():
#     response = client.post(
#         "/api/v1/users/vendedor",
#         json={"nombre": "Ana", "apellido": "Lopez", "ciudad": "Medellin", "cargo": "asesor"}
#     )
#     assert response.status_code == 200
#     assert response.json()["nombre"] == "Ana"
