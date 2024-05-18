from sqlalchemy.orm import Session
from app.models.auth import Autenticacion
from app.schemas.auth import UserCreate
from app.core.security import get_password_hash, verify_password

def create_user(db: Session, user: UserCreate):
    db_user = Autenticacion(
        nombre_usuario=user.nombre_usuario,
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Autenticacion).filter(Autenticacion.nombre_usuario == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user