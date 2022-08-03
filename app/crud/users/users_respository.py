"""
    Module for UsersRepository
"""
from typing import List, Union
from app.db import IDBRepository
from app.crud.users import IUsersRepository, User, UserDB, UserPublic
from app.configs import get_environment
from psycopg2.errors import UniqueViolation
from app.exceptions import UserNotInsertedError, UserGetError

_env = get_environment()


class UsersRepository(IUsersRepository):
    """
    This class manipulates users table
    """

    __table = "users"

    def __init__(self, connection: IDBRepository) -> None:
        super().__init__(
            db_schema=_env.POSTGRES_DB_SCHEMA, table=self.__table, connection=connection
        )

    def insert(self, dto: User) -> UserPublic:
        try:
            user = super().insert(UserDB(**dto.dict()))
            return UserPublic(**user.dict())

        except (UniqueViolation, Exception) as error:
            raise UserNotInsertedError(error.args)

    def get(self) -> List[UserPublic]:
        try:
            return super().get()

        except Exception:
            raise UserGetError()

    def get_by_id(self, id: Union[int, str]) -> UserPublic:
        try:
            return super().get_by_id(id)

        except Exception:
            raise UserGetError(f"User with id {id} not found")

    def get_by_name(self, username: str) -> UserPublic:
        return super().get_by_name(username)

    def update(self, id: Union[int, str], dto: User) -> UserPublic:
        return super().update(id, dto)

    def delete(self, id: Union[int, str]) -> UserPublic:
        return super().delete(id)
