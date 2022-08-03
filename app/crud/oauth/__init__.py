"""
    Module for oauth2
"""
from app.crud.oauth.oauth_service import get_current_active_user, get_current_user
from app.crud.oauth.oauth_view import oauth_router
