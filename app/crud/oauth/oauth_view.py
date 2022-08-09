"""
    Module for oauth
"""
from fastapi import APIRouter, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from app.crud.users import UsersService, UsersRepository, UserDB
from app.db import PostgresRepository
from app.configs import get_environment
from app.shared_schemas import Token
from datetime import timedelta
from app.utils import create_access_token
from app.crud.oauth import get_current_user

_env = get_environment()

oauth_router = APIRouter(prefix="/oauth")
repository = UsersRepository(connection=PostgresRepository())
services = UsersService(repository=repository)


@oauth_router.post("/token", response_model=Token, tags=["oauth"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = services.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User disabled",
        )

    access_token_expires = timedelta(minutes=_env.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@oauth_router.post("/verify-code", tags=["oauth"])
async def verify_code(
    code: int, current_user: UserDB = Security(get_current_user, scopes=["2FA"])
):
    return code


@oauth_router.get("/code", tags=["oauth"])
async def get_code(
    code: int, current_user: UserDB = Security(get_current_user, scopes=["2FA"])
):
    return code


@oauth_router.post("/revoke", tags=["oauth"])
async def revoke(
    code: int, current_user: UserDB = Security(get_current_user, scopes=[])
):
    return code


@oauth_router.get("/authorize", tags=["oauth"])
async def authorize(
    redirect_url: str, current_user: UserDB = Security(get_current_user, scopes=[])
):
    return RedirectResponse(redirect_url)
