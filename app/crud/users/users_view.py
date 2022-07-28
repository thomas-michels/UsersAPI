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
        response = {
            "status": 200,
            "message": "Delete user with success"
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
