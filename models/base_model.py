#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""

import models
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        else:
            # kwargs['updated_at'] = datetime.strptime(
            #     kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            # kwargs['created_at'] = datetime.strptime(
            #     kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            # del kwargs['__class__']
            # self.__dict__.update(kwargs)
            if '__class__' in kwargs:
                del kwargs['__class__']

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            else:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], DATE_FORMAT)
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()
            else:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], DATE_FORMAT)

            # Setting instance attributes from kwargs
            for key, value in kwargs.items():
                setattr(self, key, value)

    def save(self):
        """
        Updates updated_at with current time when instance is
        changed
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)

        # Remove _sa_instance_state if it exists
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        else:
            dictionary['__class__'] = (
                str(type(self)).split('.'))[-1].split('\'')[0]
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """
        Deletes the current instance from storage
        """
        models.storage.delete(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())
