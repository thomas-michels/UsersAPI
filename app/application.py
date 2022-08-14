"""
    Application file
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.crud.users import users_router
from app.crud.oauth import oauth_router
from app.crud.scopes import scopes_router


class FastAPIApplication:
    """
    FastAPIApplication class
    """

    @staticmethod
    def get_application():
        app = FastAPI(title="UsersAPI")

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.include_router(users_router)
        app.include_router(oauth_router)
        app.include_router(scopes_router)

        return app
