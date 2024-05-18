from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Autenticacion(Base):
    __tablename__ = "autenticacion"
    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)