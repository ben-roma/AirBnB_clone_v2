#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

# Many-to-Many relationship table between Place and Amenity
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    name = Column(String(128), nullable=False) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    description = Column(String(1024)) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    number_rooms = Column(Integer, default=0, nullable=False) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(Integer, default=0, nullable=False) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    max_guest = Column(Integer, default=0, nullable=False) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(Integer, default=0, nullable=False) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(Float) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(Float) \
        if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade="all, delete, delete-orphan",
                               backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals
            to the current Place.id"""
            from models import storage
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the attribute
            amenity_ids"""
            from models import storage
            return [amenity for amenity in storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Handles appending Amenity ids to the amenity_ids list"""
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
