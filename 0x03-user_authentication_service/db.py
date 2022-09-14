#!/usr/bin/env  python3
"""DB module
"""
from random import randint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str = None, hashed_password: str = None) -> User:
        """Adds a new user to database"""

        if email is None or hashed_password is None:
            return None

        new_user = User(email=email, hashed_password=hashed_password, reset_token=None, session_id=None)
        self._session.add(new_user)
        self._session.commit()

        return new_user
