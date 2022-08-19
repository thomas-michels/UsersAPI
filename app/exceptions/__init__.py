"""
    Module for exceptions
"""

from app.exceptions.postgres_errors import PostgresConnectionError
from app.exceptions.base_error import IError
from app.exceptions.users_errors import *
from app.exceptions.scopes_errors import (
    ScopeNotInsertedError,
    ScopeGetError,
    ScopeUpdateError,
)
