"""
    Module for UsersService
"""
from app.crud.users import IUsersRepository, User, UserDB, UserPublic
from typing import Union, List
from app.utils import verify_password, get_password_hash
from app.shared_schemas import Feedback
from app.exceptions import UserNotInsertedError, UserGetError


class UsersService:
    """
    This class applies business rules of User
    """

    def __init__(self, repository: IUsersRepository) -> None:
        self.__repository = repository

    def insert(self, dto: User) -> Feedback:
        try:
            feedback = Feedback()

            dto.user_password = get_password_hash(dto.user_password)
            user_inserted = self.__repository.insert(dto)

            if user_inserted:
                feedback.data.append(user_inserted)

            else:
                feedback.is_successful = False

        except UserNotInsertedError as error:
            feedback.is_successful = False
            feedback.errors.append(error)

        except Exception as error:
            feedback.is_successful = False
            feedback.errors.append(error.args)
        
        finally:
            return feedback

    def get(self) -> Feedback:
        try:
            feedback = Feedback()
            users = self.__repository.get()
            if users:
                feedback.data.extend(users)

            else:
                feedback.is_successful = False

        except UserGetError as error:
            feedback.is_successful = False
            feedback.errors.append(error)

        finally:
            return feedback

    def get_by_id(self, id: Union[int, str]) -> Feedback:
        return self.__repository.get_by_id(id)

    def update(self, id: Union[int, str], dto: User) -> Feedback:
        return self.__repository.update(id, dto)

    def delete(self, db_schema: str, table: str, id: Union[int, str]) -> Feedback:
        return self.__repository.delete(db_schema, table, id)
