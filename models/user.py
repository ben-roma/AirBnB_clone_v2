#!/usr/bin/python3
"""This module defines a class User"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        # Columns defined only for database storage
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        # Relationships
        places = relationship('Place', cascade="all, delete,
                              delete-orphan", backref='user')
        reviews = relationship('Review', cascade="all, delete,
                               delete-orphan", backref='user')
    else:
        # Simple attributes for file storage, initialized to None
        email = None
        password = None
        first_name = None
        last_name = None
        places = None
        reviews = None

    def __init__(self, **kwargs):
        """Initialize the user instance"""
        super().__init__(**kwargs)
        if storage_type != 'db':
            # Set attributes for file storage if they are passed in kwargs
            self.email = kwargs.get('email', None)
            self.password = kwargs.get('password', None)
            self.first_name = kwargs.get('first_name', None)
            self.last_name = kwargs.get('last_name', None)
