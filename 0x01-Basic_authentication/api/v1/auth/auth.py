#!/usr/bin/env python3
"""
Authenticate module class
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Class to manage the authentication for users
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Requier authenticate
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return current user
        """
        return None
