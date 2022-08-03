"""
    Module for UsersService
"""
from app.crud.users import IUsersRepository, User, UpdateUser
from typing import Union
from app.crud.users.users_schema import SimpleUser
from app.utils import verify_password, get_password_hash
from app.shared_schemas import Feedback
from app.exceptions import UserNotInsertedError, UserGetError, UserUpdateError


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
        try:
            feedback = Feedback()
            user = self.__repository.get_by_id(id)
            if user:
                feedback.data.append(user)

            else:
                feedback.is_successful = False

        except UserGetError as error:
            feedback.is_successful = False
            feedback.errors.append(error)

        finally:
            return feedback

    def get_by_name(self, username: str) -> Feedback:
        try:
            feedback = Feedback()
            user = self.__repository.get_by_name(username)
            if user:
                feedback.data.append(user)

            else:
                feedback.is_successful = False

        except UserGetError as error:
            feedback.is_successful = False
            feedback.errors.append(error)

        finally:
            return feedback

    def update(self, id: Union[int, str], dto: SimpleUser) -> Feedback:
        try:
            feedback = Feedback()
            old_user = self.__repository.get_by_id_private(id=id)
            if old_user:
                updated_user = UpdateUser()
                updated_user.user_id = id
                updated_user.username = (
                    dto.username if dto.username else old_user.username
                )
                updated_user.user_password = (
                    get_password_hash(dto.user_password)
                    if dto.user_password
                    else old_user.user_password
                )
                updated_user.email = dto.email if dto.email else old_user.email

                user_id = self.__repository.update(id, updated_user)

                if not user_id:
                    feedback.is_successful = False

            else:
                feedback.is_successful = False

        except (UserGetError, UserUpdateError) as error:
            feedback.is_successful = False
            feedback.errors.append(error)

        finally:
            return feedback

    def delete(self, id: Union[int, str]) -> Feedback:
        try:
            feedback = Feedback()
            deleted = self.__repository.delete(id=id)
            if not deleted:
                feedback.is_successful = False

        except Exception:
            feedback.is_successful = False

        finally:
            return feedback

    def authenticate_user(self, username: str, password: str):
        user = self.__repository.get_by_name_private(username)
        if not user:
            return False

        if not verify_password(password, user.user_password):
            return False

        return user
