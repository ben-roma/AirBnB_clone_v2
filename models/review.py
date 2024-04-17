#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'

    if storage_type == 'db':
        # Attributes are defined as columns when using database storage
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        # Attributes are simple strings or None for file-based storage
        place_id = None
        user_id = None
        text = None

    def __init__(self, **kwargs):
        """Initialize the review instance according to storage type"""
        super().__init__(**kwargs)
        if storage_type != 'db':
            self.place_id = kwargs.get('place_id', None)
            self.user_id = kwargs.get('user_id', None)
            self.text = kwargs.get('text', None)
