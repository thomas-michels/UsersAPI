"""
    Module for Users Routes
"""
from typing import List
from fastapi import APIRouter, Security
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud.users import (
    User,
    UserPublic,
    UsersService,
    UsersRepository,
    SimpleUser,
    UserDB,
)
from app.crud.oauth import get_current_user
from app.db import PostgresRepository


users_router = APIRouter()

repository = UsersRepository(connection=PostgresRepository())
services = UsersService(repository=repository)


@users_router.post("/users/", tags=["users"], response_model=UserPublic)
def create_users(
    user: SimpleUser,
    current_user: UserDB = Security(get_current_user, scopes=["create"]),
):
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
async def read_users_me(
    current_user: UserDB = Security(get_current_user, scopes=["me"])
):
    return JSONResponse(status_code=200, content=jsonable_encoder(current_user.dict()))


@users_router.get("/users/", tags=["users"], response_model=List[UserPublic])
def get_users(current_user: UserDB = Security(get_current_user, scopes=["read"])):
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
def get_users_by_id(
    user_id: str, current_user: UserDB = Security(get_current_user, scopes=["read"])
):
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
def update_users(
    user_id: str,
    user: SimpleUser,
    current_user: UserDB = Security(get_current_user, scopes=["update"]),
):
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
def delete_users(
    user_id: str, current_user: UserDB = Security(get_current_user, scopes=["delete"])
):
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
