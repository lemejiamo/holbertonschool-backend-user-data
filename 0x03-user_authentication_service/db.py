#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User, Base


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

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword argument"""
        filters = ('email',
                   'id',
                   'hashed_password',
                   'session_id',
                   'reset_token')
        if not kwargs:
            raise InvalidRequestError
        _key: str
        _value: str
        for key, value in kwargs.items():
            if key not in filters:
                raise InvalidRequestError
            else:
                _key = key
                _value = value
        query = {_key: _value}
        user = self._session.query(User).filter_by(**query).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the user’s attributes as passed in the method’s
        arguments then commit changes to the database.
        Takes as argument a required user_id
        """
        if user_id is None or kwargs is None:
            return None

        filters = ('email',
                   'id',
                   'hashed_password',
                   'session_id',
                   'reset_token')

        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                print(key)
                if key in filters:
                    setattr(user, key, value)
            print(user)
        except NoResultFound or InvalidRequestError:
            raise ValueError

        self._session.commit()
