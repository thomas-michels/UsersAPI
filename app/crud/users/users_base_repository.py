"""
    Module for Users Repository
"""
from typing import List, Union
from app.db import IDBRepository
from app.crud.users import User, UserPublic


class IUsersRepository:
    """
    Interface class for UsersRepository
    """

    def __init__(self, db_schema: str, table: str, connection: IDBRepository) -> None:
        self.__db_schema = db_schema
        self.__table = table
        self.__connection = connection

    def insert(self, dto: User) -> UserPublic:
        return self.__connection.insert(self.__db_schema, self.__table, dto)

    def get(self) -> List[UserPublic]:
        return self.__connection.get(self.__db_schema, self.__table, UserPublic)

    def get_by_id(self, id: Union[int, str]) -> UserPublic:
        return self.__connection.get_by_id(self.__db_schema, self.__table, id, UserPublic)

    def update(self, id: Union[int, str], dto: User) -> UserPublic:
        return self.__connection.update(self.__db_schema, self.__table, id, dto)

    def delete(self, id: Union[int, str]) -> UserPublic:
        return self.__connection.delete(self.__db_schema, self.__table, id, UserPublic)
