"""
    Module for postgres utils
"""
from datetime import datetime
from typing import Any, List
from psycopg2 import OperationalError, connect
from pydantic import BaseModel
from app.configs import get_environment, get_logger
from app.exceptions import PostgresConnectionError
from uuid import UUID

_env = get_environment()
_logger = get_logger(__name__)


def format_type(field: Any) -> str:
    """
    Function to format field to correct form in str

    :param field: Any

    :return: str
    """
    if type(field) is str or type(field) is UUID:
        return f"'{field}'"

    elif type(field) is datetime:
        return f"'{field.strftime('%Y-%m-%d %H:%M:%S')}'"

    return str(field)


def fiels_converter(dto_dict: list) -> str:
    """
    Function to return the name of fields

    :param dto_dict: list

    :return: str
    """
    return ", ".join(str(field) for field in dto_dict)


def values_converter(dto_dict: list) -> str:
    """
    Function to return formatted values

    :param dto_dict: list

    :return: str
    """
    return ", ".join(format_type(values) for values in dto_dict)


def get_dto_fields(dto: BaseModel) -> List[str]:
    return list(dto.__fields__.keys())


def mount_dto(dto: BaseModel, value: tuple) -> dict:
    value_dict = {}
    fields = get_dto_fields(dto)
    for index, field in enumerate(fields):
        value_dict[field] = value[index]

    return value_dict


def get_id_field(dto: BaseModel) -> str:
    fields = get_dto_fields(dto)
    for field in fields:
        if field.__contains__("id"):
            return field


def update_fields(dto: BaseModel) -> str:
    dto_dict = dto.dict()
    fields = dto_dict.keys()
    updated_fields = []
    for field in fields:
        updated_fields.append(f"{field} = {format_type(dto_dict[field])}")

    return ", ".join(updated_fields)


def execute_query(sql: str, many=False) -> tuple:
    """
    Function to execute queries in datebase

    :param sql: str

    :param many: default False

    :return: tuple
    """
    try:
        conn = connect(
            f"host={_env.POSTGRES_DB_HOST}"            
            f" port={_env.POSTGRES_DB_PORT}"            
            f" dbname={_env.POSTGRES_DB_NAME}"
            f" user={_env.POSTGRES_DB_USER}"
            f" password={_env.POSTGRES_DB_PASSWORD}"
        )

        cursor = conn.cursor()
        cursor.execute(sql)

        if not sql.__contains__("UPDATE") and not sql.__contains__("DELETE"):
            data = cursor.fetchall() if many else cursor.fetchone()

        else:
            data = True

        conn.commit()
        conn.close()

        return data

    except OperationalError:
        _logger.error(f"Error in postgres connection")
        raise PostgresConnectionError()
