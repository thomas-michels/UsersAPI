"""
Module to load all Environment variables
"""

from pydantic import BaseSettings
from typing import List


class Environment(BaseSettings):
    """
    Environment, add the variable and its type here matching the .env file
    """

    POSTGRES_DB_NAME: str
    POSTGRES_DB_USER: str
    POSTGRES_DB_PASSWORD: str
    POSTGRES_DB_SCHEMA: str
    HASH_SCHEMES: str
    HASH_DEPRECATED: str
    POSTGRES_DB_HOST: str
    POSTGRES_DB_PORT: int
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        """Load config file"""

        env_file = ".env"
