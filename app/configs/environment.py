"""
Module to load all Environment variables
"""

from pydantic import BaseSettings


class Environment(BaseSettings):
    """
    Environment, add the variable and its type here matching the .env file
    """

    POSTGRES_DB_NAME: str
    POSTGRES_DB_USER: str
    POSTGRES_DB_PASSWORD: str
    POSTGRES_DB_SCHEMA: str

    class Config:
        """Load config file"""

        env_file = ".env"

