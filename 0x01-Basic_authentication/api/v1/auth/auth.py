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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1:] == "/":
            if path in excluded_paths:
                return False
        else:
            for ex_path in excluded_paths:
                if path == ex_path[:-1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        if request is None:
            return None
        print(request.headers.get('Authorization'))
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return current user
        """
        return None
