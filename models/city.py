#!/usr/bin/python3
"""Defines the City class."""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", back_populates="cities",
                          cascade="all, delete, delete-orphan")
