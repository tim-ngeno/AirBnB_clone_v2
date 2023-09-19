#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"),
                         nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)

        # Create relationship with User and City
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
