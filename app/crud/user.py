from sqlalchemy.orm import Session
from app.models.user import User,Comprador,Vendedor
from app.schemas.user import CompradorCreate, UserBase, VendedorCreate
from sqlalchemy.exc import SQLAlchemyError

def get_user(db:Session,user_id:int):
    return db.query(User).filter(User.id==user_id).first()

def update_user(db: Session, user_id: int, user: UserBase):
    db_user = get_user(db, user_id)
    if db_user:
        # if isinstance(db_user, Comprador):
        #     db_user.direccion = user.direccion
        # if isinstance(db_user, Vendedor):
        #     db_user.cargo = user.cargo
        db_user.nombre = user.nombre
        db_user.apellido = user.apellido
        db_user.ciudad = user.ciudad
        db.commit()
        db.refresh(db_user)
        return db_user
    return None


def get_users(db:Session,skip: int=0 , limit: int=10):
    return db.query(User).offset(skip).limit(limit).all()

def create_comprador(db: Session, user: CompradorCreate, longitud: float = 0, latitud: float = 0, estado_geo: str = "unknown"):
    try:
        db_user = Comprador(
            nombre=user.nombre,
            apellido=user.apellido,
            ciudad=user.ciudad,
            direccion=user.direccion,
            longitud=longitud,
            latitud=latitud,
            estado_geo=estado_geo,
            tipo='comprador'
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating Comprador: {e}")
        raise
    except TypeError as e:
        db.rollback()
        print(f"Type error creating Comprador: {e}")
        raise
    

def create_vendedor(db:Session,user:VendedorCreate):
    db_user=Vendedor(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, user_id:int):
    db_user=db.query(User).filter(User.id==user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def update_comprador(db: Session,user_id:int , user:CompradorCreate):
    db_user=db.query(Comprador).filter(Comprador.id ==user_id).first()
    if db_user:
        for key, value in user.model_dump().items():
            setattr(db_user,key,value)
        db.commit()
        db.refresh(db_user)
    return db_user

def update_vendedor(db:Session,user_id: int, user:VendedorCreate):
    db_user=db.query(Vendedor).filter(Vendedor.id==user_id).first()
    if db_user:
        for key,value in user.model_dump().items():
            setattr(db_user,key,value)
            db.commit()
            db.refresh(db_user)
    return db_user