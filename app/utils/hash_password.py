"""
    Module to generate hashed password
"""
from passlib.context import CryptContext
from app.configs import get_environment

_env = get_environment()


pwd_context = CryptContext(schemes=_env.HASH_SCHEMES, deprecated=_env.HASH_DEPRECATED)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)
