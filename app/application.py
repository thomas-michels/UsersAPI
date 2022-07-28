"""
    Application file
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.crud.users import users_router


class FastAPIApplication:
    """
    FastAPIApplication class
    """

    @staticmethod
    def get_application():
        app = FastAPI()

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.include_router(users_router)

        return app
