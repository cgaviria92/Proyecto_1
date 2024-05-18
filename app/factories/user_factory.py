from app import schemas, crud
from app.utils.geocoder import geocode_address

def create_comprador(db, user: schemas.CompradorCreate):
    longitud, latitud, estado_geo = geocode_address(user.direccion, user.ciudad)
    return crud.create_comprador(db, user=user, longitud=longitud, latitud=latitud, estado_geo=estado_geo)

def create_vendedor(db, user: schemas.VendedorCreate):
    return crud.create_vendedor(db, user=user)
