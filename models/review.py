#!/usr/bin/python3
""" Review module for the HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """ Review class to map Review module to a table """

    __tablename__ = "reviews"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"),
                          nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"),
                         nullable=False)

        user = relationship("User", back_populates="reviews")
        places = relationship("Place", back_populates="reviews")

    else:
        text = ""
        place_id = ""
        user_id = ""
