"""
    Module for Users errors
"""
from app.exceptions import IError


class ScopeNotInsertedError(IError):
    """
    Raised when happen error in insert new scope
    """

    def __init__(self, message: str = "Error in insert Scope") -> None:
        code = 10
        super().__init__(code, message)


class ScopeGetError(IError):
    """
    Raised when happen error in get scope
    """

    def __init__(self, message: str = "Error in get Scope") -> None:
        code = 14
        super().__init__(code, message)


class ScopeUpdateError(IError):
    """
    Raised when happen error in update scope
    """

    def __init__(self, message: str = "Error in update Scope") -> None:
        code = 12
        super().__init__(code, message)
