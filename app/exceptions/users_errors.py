"""
    Module for Users errors
"""
from app.exceptions import IError


class UserNotInsertedError(IError):
    """
    Raised when happen error in insert new user
    """

    def __init__(self, message: str = "Error in insert User") -> None:
        code = 10
        super().__init__(code, message)


class UserGetError(IError):
    """
    Raised when happen error in get user
    """

    def __init__(self, message: str = "Error in get User") -> None:
        code = 14
        super().__init__(code, message)


class UserUpdateError(IError):
    """
    Raised when happen error in update user
    """

    def __init__(self, message: str = "Error in update User") -> None:
        code = 12
        super().__init__(code, message)
