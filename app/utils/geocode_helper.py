from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import Comprador
from app.utils.geocoder import geocode_address

db=Session()

def geocode_and_update_users(db):
    users = db.query(Comprador).filter(
        or_(
            Comprador.longitud == None,
            Comprador.latitud == None,
            Comprador.longitud == 0,
            Comprador.latitud == 0,
            Comprador.longitud == '',
            Comprador.latitud == ''
        )
    ).all()
    updated_count = 0
    for user in users:
        user.longitud, user.latitud, user.estado_geo = geocode_address(user.direccion, user.ciudad)
        db.commit()
        updated_count += 1
    return updated_count
