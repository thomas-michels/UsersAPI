"""
    Application file
"""
from fastapi import FastAPI


class FastAPIApplication:
    """
    FastAPIApplication class
    """

    @staticmethod
    def get_application():
        app = FastAPI()

        return app
