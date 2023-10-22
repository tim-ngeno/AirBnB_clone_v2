#!/usr/bin/python3
"""
New engine that connects to the database and also sets up SQLAlchemy
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Handles storage for the database using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance with engine."""
        username = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        database = os.getenv("HBNB_MYSQL_DB")
        db_uri = "mysql+mysqldb://{}:{}@{}/{}".format(
            username, password, host, database
        )
        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Query all objects of a given class, or all classes if None.

        Args:
            cls (class): The class type to query for.

        Returns:
            dict: A dictionary of all objects.
        """
        result = {}
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls_obj in classes:
                objects = self.__session.query(cls_obj).all()
                for obj in objects:
                    key = "{}.{}".format(cls_obj.__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """
        Add a new object to the current database session.

        Args:
            obj (BaseModel): The object to add.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session.

        Args:
            obj (BaseModel, optional): The object to delete.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload all tables in the database and establish a new
        session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        ScopedSession = scoped_session(session_factory)
        self.__session = ScopedSession()

    def close(self):
        """Close and remove the current database session."""
        if self.__session:
            self.__session.close()
