"""
    Module for Users Repository
"""
from typing import List, Union
from app.crud.scopes import ScopeSchema, ScopeInDBSchema, UpdateScopeSchema
from app.db import IDBRepository


class IScopesRepository:
    """
    Interface class for ScopesRepository
    """

    def __init__(self, db_schema: str, table: str, connection: IDBRepository) -> None:
        self.__db_schema = db_schema
        self.__table = table
        self.__connection = connection

    def insert(self, dto: ScopeSchema) -> ScopeInDBSchema:
        return self.__connection.insert(self.__db_schema, self.__table, dto)

    def get(self) -> List[ScopeInDBSchema]:
        return self.__connection.get(self.__db_schema, self.__table, ScopeInDBSchema)

    def get_by_id(self, id: Union[int, str]) -> ScopeInDBSchema:
        return self.__connection.get_by_id(self.__db_schema, self.__table, id, ScopeInDBSchema)

    def update(self, id: Union[int, str], dto: UpdateScopeSchema) -> ScopeInDBSchema:
        return self.__connection.update(self.__db_schema, self.__table, id, dto)

    def delete(self, id: Union[int, str]) -> ScopeInDBSchema:
        return self.__connection.delete(self.__db_schema, self.__table, id, ScopeInDBSchema)
