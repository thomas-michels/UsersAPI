"""
    Module for Postgres repository
"""
from app.db.idb_repository import IDBRepository
from pydantic import BaseModel
from typing import List, Union
from app.utils import (
    fiels_converter,
    values_converter,
    execute_query,
    mount_dto,
    get_dto_fields,
    get_id_field,
    update_fields,
    format_type
)


class PostgresRepository(IDBRepository):
    """
    Class to connect in database and execute some query
    """

    def insert(self, db_schema: str, table: str, dto: BaseModel) -> BaseModel:
        dto_dict = dto.dict()
        fields = fiels_converter(dto_dict.keys())
        values = values_converter(dto_dict.values())
        query = f"""
        INSERT INTO {db_schema}.{table}({fields})
         VALUES ({values})
         RETURNING {fields};
        """
        if execute_query(sql=query):
            return dto

    def get(self, db_schema: str, table: str, dto: BaseModel) -> List[BaseModel]:
        fields = fiels_converter(get_dto_fields(dto))
        query = f"""
        SELECT {fields} FROM {db_schema}.{table};
        """
        values = execute_query(sql=query, many=True)
        return [dto(**mount_dto(dto, value)) for value in values]

    def get_by_id(
        self, db_schema: str, table: str, id: Union[int, str], dto: BaseModel
    ) -> BaseModel:
        fields = fiels_converter(get_dto_fields(dto))
        query = f"""
        SELECT {fields} FROM {db_schema}.{table} WHERE {get_id_field(dto)} = {format_type(id)};
        """
        value = execute_query(sql=query)
        return dto(**mount_dto(dto, value))

    def update(
        self, db_schema: str, table: str, id: Union[int, str], dto: BaseModel
    ) -> BaseModel:
        query = f"""
        UPDATE {db_schema}.{table}
         SET {update_fields(dto)}
         WHERE {get_id_field(dto.__class__)} = {format_type(id)};
        """
        value = execute_query(sql=query)
        return id if value else False

    def delete(
        self, db_schema: str, table: str, id: Union[int, str], dto: BaseModel
    ) -> BaseModel:
        query = f"""
        DELETE FROM {db_schema}.{table} WHERE {get_id_field(dto)} = {format_type(id)};
        """
        value = execute_query(sql=query)
        return id if value else False
