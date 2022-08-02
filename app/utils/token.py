from typing import Union
from datetime import datetime, timedelta
from app.configs import get_environment
from jose import JWTError, jwt

_env = get_environment()


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, _env.SECRET_KEY, algorithm=_env.ALGORITHM)
    return encoded_jwt
