#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)

        # Create a relationship with cities
        cities = relationship("City", back_populates="state",
                              cascade="all, delete, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """
            Returns the list of City objects linked to current state
            """
            all_cities = models.storage.all(City)
            linked_cities = [
                city for city in all_cities.values() if
                city.state_id == self.id
            ]
            return linked_cities
