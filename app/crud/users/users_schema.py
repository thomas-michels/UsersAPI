"""
    Module for Users Schemas
"""
from pydantic import BaseModel, EmailStr
from pydantic import Field
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional


class SimpleUser(BaseModel):
    """
    Schema for SimpleUser
    """

    username: str = Field(example="thomas")
    user_password: str = Field(example="teste123")
    email: EmailStr = Field(example="example@example.com")


class User(SimpleUser):
    """
    Schema for User
    """

    created_on: datetime = Field(default_factory=datetime.now, example="")
    last_login: Optional[datetime] = Field(default_factory=datetime.now, example="")

    class Config:
        json_encoders = {
            "created_on": lambda date: str(date),
            "last_login": lambda date: str(date),
        }


class UserDB(User):
    """
    Schema for UserDB
    """

    user_id: UUID = Field(
        default_factory=uuid4, example="f6f80575-759d-48d2-9a58-fe7e2c26d41d"
    )


class UserPublic(BaseModel):
    """
    Schema for UserPublic
    """

    user_id: UUID = Field(
        default_factory=uuid4, example="f6f80575-759d-48d2-9a58-fe7e2c26d41d"
    )
    username: str = Field(example="thomas")
    email: EmailStr = Field(example="example@example.com")
    created_on: datetime = Field(default_factory=datetime.now, example="")
    last_login: Optional[datetime] = Field(default_factory=datetime.now, example="")

    class Config:
        json_encoders = {
            "created_on": lambda date: str(date),
            "last_login": lambda date: str(date),
        }
