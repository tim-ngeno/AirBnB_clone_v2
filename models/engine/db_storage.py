#!/usr/bin/python3
""" New engine that connects to the database and also sets up SQLAlchemy"""

import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import classes
import models


class DBStorage:
    """ Defines class """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes SQLAlchemy engine """
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    user, passwd, host, db), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns dictionary of objects in database"""
        dict_obj = {}
        obj = [v for k, v in classes.items()]
        if cls:
            if isinstance(cls, str):
                cls = classes[cls]
            obj = [cls]
        for i in obj:
            for instance in self.__session.query(c):
                key = str(instance.__class__.name__) + "." str(instance.id)
                dict_obj[key] = instance
        return (dict_obj)

    def new(self, obj):
        """ Adds object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from current db session if obj is not None """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Creates all tables in the database
        creates current db session from self.__session using session maker"""
        Base.metadata.create_all(self.__engine)
        db_session = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Defines close method """
        if self.__session:
            self.__session.close()
