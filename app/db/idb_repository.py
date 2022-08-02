"""
    Module for interface of DB repository
"""

from abc import ABC, abstractmethod
from typing import List, Union
from pydantic import BaseModel


class IDBRepository(ABC):
    """
    Abstract class for DB repository
    """

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    @abstractmethod
    def insert(self, db_schema: str, table: str, dto: BaseModel) -> BaseModel:
        """
        Method to insert data in database

        :param db_schema: Name of DB Schema

        :param table: Name of table

        :param dto: DataTransferObject

        :return: BaseModel
        """
        raise NotImplementedError("Insert not implemented!")

    @abstractmethod
    def get(self, db_schema: str, table: str, dto: BaseModel) -> List[BaseModel]:
        """
        Method to get data in database

        :param db_schema: Name of DB Schema

        :param table: Name of table

        :param dto: DataTransferObject

        :return: List[BaseModel]
        """
        raise NotImplementedError("Get not implemented!")

    @abstractmethod
    def get_by_id(
        self, db_schema: str, table: str, id: Union[int, str], dto: BaseModel
    ) -> BaseModel:
        """
        Method to get by id data in database

        :param db_schema: Name of DB Schema

        :param table: Name of table

        :param id: Union[int, str]

        :param dto: DataTransferObject

        :return: BaseModel
        """
        raise NotImplementedError("Get by ID not implemented!")

    @abstractmethod
    def get_by_name(
        self, db_schema: str, table: str, name: str, dto: BaseModel
    ) -> BaseModel:
        """
        Method to get by name data in database

        :param db_schema: Name of DB Schema

        :param table: Name of table

        :param name: str

        :param dto: DataTransferObject

        :return: BaseModel
        """
        raise NotImplementedError("Get by name not implemented!")

    @abstractmethod
    def update(
        self, db_schema: str, table: str, id: Union[int, str], dto: BaseModel
    ) -> BaseModel:
        """
        Method to update data in database

        :param db_schema: Name of DB Schema

        :param table: Name of table

        :param id: Union[int, str]

        :param dto: DataTransferObject

        :return: BaseModel
        """
        raise NotImplementedError("Update not implemented!")

    @abstractmethod
    def delete(
        self, db_schema: str, table: str, id: Union[int, str], dto: BaseModel
    ) -> BaseModel:
        """
        Method to delete data in database

        :param db_schema: Name of DB Schema

        :param table: Name of table

        :param id: Union[int, str]

        :param dto: DataTransferObject

        :return: BaseModel
        """
        raise NotImplementedError("Delete not implemented!")
