"""
    Module for Feedback
"""
from typing import List, Optional
from pydantic import BaseModel
from app.exceptions import IError


class Feedback(BaseModel):
    """
    Schema for Feedback
    """

    is_successful: bool = True
    data: Optional[List[BaseModel]] = []
    errors: Optional[List[IError]] = []

    class Config:
        arbitrary_types_allowed = True
