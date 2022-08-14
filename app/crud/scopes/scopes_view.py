# """
#     Module for Users Routes
# """
# from typing import List
# from fastapi import APIRouter, Security
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder
# from app.crud.scopes import (
#     ScopeInDBSchema, ScopeSchema, UpdateScopeSchema
# )
# from app.crud.oauth import get_current_user
# # from app.db import PostgresRepository


# scopes_router = APIRouter()

# # repository = UsersRepository(connection=PostgresRepository())
# # services = UsersService(repository=repository)


# @scopes_router.post("/scopes/", tags=["scopes"], response_model=ScopeInDBSchema)
# def create_scopes(
#     scope: ScopeSchema,
#     current_user: UserDB = Security(get_current_user, scopes=["admin"]),
# ):
#     """
#     Route to create new user
#     """
#     feedback = services.insert(User(**user.dict()))
#     if feedback.is_successful:
#         response = {
#             "status": 201,
#             "message": "New user created with success",
#             "data": feedback.data[0].dict(),
#         }

#     else:
#         response = {
#             "status": 422,
#             "message": "Error on create new user",
#             "errors": [error.serialize() for error in feedback.errors],
#         }

#     return JSONResponse(
#         status_code=response["status"], content=jsonable_encoder(response)
#     )


# @scopes_router.get("/scopes/", tags=["scopes"], response_model=List[ScopeInDBSchema])
# def get_scopes(current_user: UserDB = Security(get_current_user, scopes=["read"])):
#     """
#     Route to get user
#     """
#     feedback = services.get()
#     if feedback.is_successful:
#         response = {
#             "status": 200,
#             "message": "Get all scopes with success",
#             "data": [scope.dict() for scope in feedback.data],
#         }

#     else:
#         response = {
#             "status": 400,
#             "message": "Error on get all scopes",
#             "errors": [error.serialize() for error in feedback.errors],
#         }

#     return JSONResponse(
#         status_code=response["status"], content=jsonable_encoder(response)
#     )


# @scopes_router.get("/scopes/{scope_id}", tags=["scopes"], response_model=ScopeInDBSchema)
# def get_scopes_by_id(
#     scope_id: str, current_user: UserDB = Security(get_current_user, scopes=["read"])
# ):
#     """
#     Route to get user by id
#     """
#     feedback = services.get_by_id(id=scope_id)
#     if feedback.is_successful:
#         response = {
#             "status": 200,
#             "message": "Get scope with success",
#             "data": feedback.data[0].dict(),
#         }

#     else:
#         response = {
#             "status": 404,
#             "message": "Error on get all scopes",
#             "errors": [error.serialize() for error in feedback.errors],
#         }

#     return JSONResponse(
#         status_code=response["status"], content=jsonable_encoder(response)
#     )


# @scopes_router.put("/scopes/{scope_id}", tags=["scopes"], response_model=ScopeInDBSchema)
# def update_scopes(
#     scope_id: str,
#     scope: UpdateScopeSchema,
#     current_user: UserDB = Security(get_current_user, scopes=["update"]),
# ):
#     """
#     Route to update scope
#     """
#     feedback = services.update(id=scope_id, dto=scope)
#     if feedback.is_successful:
#         response = {"status": 200, "message": "Updated with success"}

#     else:
#         response = {
#             "status": 404,
#             "message": "Error on get all scopes",
#             "errors": [error.serialize() for error in feedback.errors],
#         }

#     return JSONResponse(
#         status_code=response["status"], content=jsonable_encoder(response)
#     )


# @scopes_router.delete("/scopes/{scope_id}", tags=["scopes"], response_model=ScopeInDBSchema)
# def delete_scopes(
#     scope_id: str, current_user: UserDB = Security(get_current_user, scopes=["delete"])
# ):
#     """
#     Route to delete scope
#     """
#     feedback = services.delete(id=scope_id)
#     if feedback.is_successful:
#         response = {"status": 200, "message": "Delete scope with success"}

#     else:
#         response = {
#             "status": 404,
#             "message": "Error on delete scopes",
#             "errors": [error.serialize() for error in feedback.errors],
#         }

#     return JSONResponse(
#         status_code=response["status"], content=jsonable_encoder(response)
#     )
