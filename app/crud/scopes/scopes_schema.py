"""
    Module for Scopes
"""
from dataclasses import Field
from typing import Optional
from pydantic import BaseModel


class ScopeSchema(BaseModel):
    """
    Schema for Scope
    """

    scope_name: str = Field(example="Read")


class ScopeInDBSchema(ScopeSchema):
    """
    Schema for ScopeInDB
    """

    scope_id: int = Field(example=123)


class UpdateScopeSchema(BaseModel):
    """
    Schema for Update scope
    """

    scope_name: Optional[str] = Field(example="Read")
