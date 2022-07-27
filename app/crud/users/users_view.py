"""
    Module for Users Routes
"""
from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud.users import User, UserPublic, UsersService, UsersRepository, SimpleUser
from app.db import PostgresRepository


users_router = APIRouter()


repository = UsersRepository(connection=PostgresRepository())
services = UsersService(repository=repository)


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
            "data": [user.dict() for user in feedback.data],
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
