"""
    Module for oauth service
"""
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    SecurityScopes,
)
from app.crud.users import UsersService, UsersRepository, UserDB
from app.db import PostgresRepository
from jose import JWTError, jwt
from app.configs import get_environment
from app.shared_schemas import TokenData
from pydantic import ValidationError

_env = get_environment()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=_env.AUTH_URL,
    scopes={
        "me": "Read information about the current user.",
        "update": "Update information.",
        "create": "Create information.",
        "delete": "Delete information.",
        "read": "Read information.",
    },
)

repository = UsersRepository(connection=PostgresRepository())
services = UsersService(repository=repository)


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'

    else:
        authenticate_value = "Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )

    try:
        payload = jwt.decode(token, _env.SECRET_KEY, algorithms=[_env.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)

    except (JWTError, ValidationError):
        raise credentials_exception

    user = repository.get_by_name_private(username=token_data.username)

    if not user:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
    current_user: UserDB = Security(get_current_user, scopes=["me"])
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
