from pydantic import BaseModel

class UserCreate(BaseModel):
    nombre_usuario: str
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserResponse(BaseModel):
    id: int
    nombre_usuario: str

    class Config:
        orm_mode = True