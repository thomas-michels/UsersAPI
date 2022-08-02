"""
    Module for Users Routes
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud.users import User, UserPublic, UsersService, UsersRepository, SimpleUser
from app.db import PostgresRepository
from jose import JWTError, jwt
from app.configs import get_environment
from app.shared_schemas import Token, TokenData
from pydantic import ValidationError
from datetime import timedelta, datetime
from app.utils import create_access_token

_env = get_environment()


users_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)

repository = UsersRepository(connection=PostgresRepository())
services = UsersService(repository=repository)


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'

    else:
        authenticate_value = f"Bearer"

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
    current_user: User = Security(get_current_user, scopes=["me"])
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@users_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = services.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=_env.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@users_router.post("/users/", tags=["users"], response_model=UserPublic)
def create_users(user: SimpleUser):
    """
    Route to create new user
    """
    feedback = services.insert(User(**user.dict()))
    if feedback.is_successful:
        response = {
            "status": 201,
            "message": "New user created with success",
            "data": feedback.data[0].dict(),
        }

    else:
        response = {
            "status": 422,
            "message": "Error on create new user",
            "errors": [error.serialize() for error in feedback.errors],
        }

    return JSONResponse(
        status_code=response["status"], content=jsonable_encoder(response)
    )


@users_router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return JSONResponse(
        status_code=200, content=jsonable_encoder(current_user.dict())
    )


@users_router.get("/users/", tags=["users"], response_model=List[UserPublic])
def get_users():
    """
    Route to get user
    """
    feedback = services.get()
    if feedback.is_successful:
        response = {
            "status": 200,
            "message": "Get all users with success",
            "data": [user.dict() for user in feedback.data],
        }

    else:
        response = {
            "status": 400,
            "message": "Error on get all users",
            "errors": [error.serialize() for error in feedback.errors],
        }

    return JSONResponse(
        status_code=response["status"], content=jsonable_encoder(response)
    )


@users_router.get("/users/{user_id}", tags=["users"], response_model=UserPublic)
def get_users_by_id(user_id: str):
    """
    Route to get user by id
    """
    feedback = services.get_by_id(id=user_id)
    if feedback.is_successful:
        response = {
            "status": 200,
            "message": "Get user with success",
            "data": feedback.data[0].dict(),
        }

    else:
        response = {
            "status": 404,
            "message": "Error on get all users",
            "errors": [error.serialize() for error in feedback.errors],
        }

    return JSONResponse(
        status_code=response["status"], content=jsonable_encoder(response)
    )


@users_router.put("/users/{user_id}", tags=["users"], response_model=UserPublic)
def update_users(user_id: str, user: SimpleUser):
    """
    Route to update user
    """
    feedback = services.update(id=user_id, dto=user)
    if feedback.is_successful:
        response = {"status": 200, "message": "Updated with success"}

    else:
        response = {
            "status": 404,
            "message": "Error on get all users",
            "errors": [error.serialize() for error in feedback.errors],
        }

    return JSONResponse(
        status_code=response["status"], content=jsonable_encoder(response)
    )


@users_router.delete("/users/{user_id}", tags=["users"], response_model=UserPublic)
def delete_users(user_id: str):
    """
    Route to delete user
    """
    feedback = services.delete(id=user_id)
    if feedback.is_successful:
        response = {"status": 200, "message": "Delete user with success"}

    else:
        response = {
            "status": 404,
            "message": "Error on get all users",
            "errors": [error.serialize() for error in feedback.errors],
        }

    return JSONResponse(
        status_code=response["status"], content=jsonable_encoder(response)
    )


@users_router.get("/users/me/items/")
async def read_own_items(
    current_user: User = Security(get_current_active_user, scopes=["items"])
):
    return [{"item_id": "Foo", "owner": current_user.username}]
