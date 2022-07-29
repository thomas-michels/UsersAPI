"""
    Module for base errors class
"""


class IError(Exception):
    """
    Interface class for errors
    """

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message

    def serialize(self) -> dict:
        return {
            "code": self.code,
            "message": self.message
        }
