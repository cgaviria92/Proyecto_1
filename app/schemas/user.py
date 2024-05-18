from pydantic import BaseModel, Field

class UserBase(BaseModel):
    nombre: str
    apellido: str
    ciudad: str

class CompradorCreate(BaseModel):
    nombre: str
    apellido: str
    ciudad: str
    direccion: str

    class Config:
        orm_mode = True


class VendedorCreate(UserBase):
    cargo: str = Field(..., pattern="^(asesor|cajero)$")

class User(UserBase):
    id: int
    tipo: str

    class Config:
        orm_mode = True

class Comprador(User):
    direccion: str
    longitud: float = None
    latitud: float = None
    estado_geo: str = None

class Vendedor(User):
    cargo: str
