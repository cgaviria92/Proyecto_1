from fastapi import APIRouter
from app.api.v1.endpoints import geocode, user,auth

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])

api_router.include_router(geocode.router, prefix="/geocoding", tags=["geocoding"])

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])