import datetime
import cachetools
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.auth import Autenticacion
from app.utils.geocode_helper import geocode_and_update_users

router = APIRouter()

# Crear un caché con tiempo de vida (TTL) de 24 horas (86400 segundos)
last_execution_cache = cachetools.TTLCache(maxsize=1, ttl=86400)

@router.get("/geocodificar_base")
def perform_geocoding(db: Session = Depends(get_db),current_user: Autenticacion = Depends(get_current_user)):
    operation = "geocodificar_base"

    # Comprobar si la operación ya se ejecutó dentro del TTL
    if operation in last_execution_cache:
        raise HTTPException(status_code=403, detail="This operation can only be executed once every 24 hours.")
    
    # Actualizar el caché con la hora actual
    last_execution_cache[operation] = datetime.datetime.utcnow()
    
    updated_count = geocode_and_update_users(db)
    return {"detail": "Geocoding completed", "updated_records": updated_count}


