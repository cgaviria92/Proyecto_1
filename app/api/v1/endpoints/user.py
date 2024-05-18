from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, auth
from app.db.session import get_db
from app.factories.user_factory import create_comprador, create_vendedor
from app.core.deps import get_current_user
from app.models.auth import Autenticacion
router = APIRouter()

@router.post("/comprador", response_model=schemas.Comprador)
def create_comprador_endpoint(user: schemas.CompradorCreate, db: Session = Depends(get_db),current_user: Autenticacion = Depends(get_current_user)):
    return create_comprador(db=db, user=user)

@router.post("/vendedor", response_model=schemas.Vendedor)
def create_vendedor_endpoint(user: schemas.VendedorCreate, db: Session = Depends(get_db),current_user: Autenticacion = Depends(get_current_user)):
    return create_vendedor(db=db, user=user)

@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: Autenticacion = Depends(get_current_user)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db),current_user: Autenticacion = Depends(get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db),current_user: Autenticacion = Depends(get_current_user)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserBase, db: Session = Depends(get_db),current_user: Autenticacion = Depends(get_current_user)):
    db_user = crud.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

