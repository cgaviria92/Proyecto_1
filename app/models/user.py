from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base_class import Base

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    apellido = Column(String, index=True, nullable=False)
    ciudad = Column(String, index=True, nullable=False)
    tipo = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_on': tipo,
        'polymorphic_identity': 'usuario'
    }

class Comprador(User):
    __tablename__ = "compradores"
    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    direccion = Column(String, nullable=False)
    longitud = Column(Float, nullable=True)
    latitud = Column(Float, nullable=True)
    estado_geo = Column(String, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'comprador'
    }

class Vendedor(User):
    __tablename__ = "vendedores"
    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    cargo = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'vendedor'
    }
