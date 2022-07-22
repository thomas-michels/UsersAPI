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
    def insert(self, db_schema: str, table: str, dto: BaseModel) -> str:
        """
        Method to insert data in database

        :db_schema param: Name of DB Schema
        :table param: Name of table
        :dto param: DataTransferObject

        :return: ID
        """
        raise NotImplementedError("Insert not implemented!")

    @abstractmethod
    def get(self, db_schema: str, table: str) -> List[object]:
        """
        Method to get data in database

        :db_schema param: Name of DB Schema
        :table param: Name of table

        :return: List[object]
        """
        raise NotImplementedError("Get not implemented!")

    @abstractmethod
    def get_by_id(self, db_schema: str, table: str, id: Union[int, str]) -> object:
        """
        Method to get by id data in database

        :db_schema param: Name of DB Schema
        :table param: Name of table
        :id param: int or str

        :return: object
        """
        raise NotImplementedError("Get by ID not implemented!")

    @abstractmethod
    def update(
        self, db_schema: str, table: str, id: Union[int, str], dto: BaseModel
    ) -> str:
        """
        Method to update data in database

        :db_schema param: Name of DB Schema
        :table param: Name of table
        :id param: int or str
        :dto param: DataTransferObject

        :return: ID
        """
        raise NotImplementedError("Update not implemented!")

    @abstractmethod
    def delete(self, db_schema: str, table: str, id: Union[int, str]) -> str:
        """
        Method to delete data in database

        :db_schema param: Name of DB Schema
        :table param: Name of table
        :id param: int or str

        :return: ID
        """
        raise NotImplementedError("Delete not implemented!")
