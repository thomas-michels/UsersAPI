"""
    Application file
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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

        return app
