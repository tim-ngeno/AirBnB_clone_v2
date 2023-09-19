#!/usr/bin/python3
"""
DB Storage module
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    Defines a DB storage class to handle storage in the database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a DBStorage instance
        """
        username = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        database = os.getenv("HBNB_MYSQL_DB")
        DB_URI = "mysql+mysqldb://{}:{}@{}/{}".format(
            username, password, host, database
        )
        self.__engine = create_engine(DB_URI, pool_pre_ping=True)

        # Drop table if in test environment
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Query all objects of a given class, or all if None
        """
        result = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
        else:
            classes = [
                "User", "State", "City", "Amenity", "Place", "Review"
            ]
            for name in classes:
                for obj in self.__session.query(eval(name)).all():
                    key = "{}.{}".format(name, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """
        Add a new object to current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload all tables in the database and establish session
        """
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        ScopedSession = scoped_session(Session)
        self.__session = ScopedSession()
