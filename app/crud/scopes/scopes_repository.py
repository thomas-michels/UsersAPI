# """
#     Module for ScopesRepository
# """
# from typing import List, Union
# from app.db import IDBRepository
# from app.crud.scopes import ScopeSchema, ScopeInDBSchema, IScopesRepository, UpdateScopeSchema
# from app.configs import get_environment
# from psycopg2.errors import UniqueViolation
# from app.exceptions import UserNotInsertedError, UserGetError

# _env = get_environment()


# class ScopesRepository(IScopesRepository):
#     """
#     This class manipulates scopes table
#     """

#     __table = "scopes"

#     def __init__(self, connection: IDBRepository) -> None:
#         super().__init__(
#             db_schema=_env.POSTGRES_DB_SCHEMA, table=self.__table, connection=connection
#         )

#     def insert(self, dto: ScopeSchema) -> ScopeInDBSchema:
#         try:
#             return super().insert(ScopeInDBSchema(**dto.dict()))

#         except (UniqueViolation, Exception) as error:
#             raise UserNotInsertedError(error.args)

#     def get(self) -> List[ScopeInDBSchema]:
#         try:
#             return super().get()

#         except Exception:
#             raise UserGetError()

#     def get_by_id(self, id: Union[int, str]) -> ScopeInDBSchema:
#         try:
#             return super().get_by_id(id)

#         except Exception:
#             raise UserGetError(f"Scope with id {id} not found")

#     def update(self, id: Union[int, str], dto: ScopeSchema) -> ScopeInDBSchema:
#         return super().update(id, dto)

#     def delete(self, id: Union[int, str]) -> ScopeInDBSchema:
#         return super().delete(id)
