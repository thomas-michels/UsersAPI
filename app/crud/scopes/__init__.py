"""
    Module for Scopes
"""

from app.crud.scopes.scopes_schema import ScopeInDBSchema, ScopeSchema, UpdateScopeSchema
from app.crud.scopes.scopes_view import scopes_router
from app.crud.scopes.scopes_base_repository import IScopesRepository
from app.crud.scopes.scopes_repository import ScopesRepository
