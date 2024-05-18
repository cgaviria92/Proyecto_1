# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TOKEN_CARLOS = "Tokensecreto"

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     if token != TOKEN_CARLOS:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Credenciales invalidad",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return {"username": "fakeuser"}
