from fastapi import FastAPI
from app.db.session import engine
from app.db.base_class import Base
from app.api.v1.api import api_router

# Importa todos los modelos para que Base conozca sus clases
from app.models import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


#url de prueba pruebas unitarias
@app.get("/")
async def root():
    return {"message": "Hello World"}