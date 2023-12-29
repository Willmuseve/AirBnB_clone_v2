#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel):
    """ State class """
    # name = ""
     __tablename__ = 'states'


    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """
            Returns the list of City objects
            from storage linked to the current State
            """
            from models import storage
            from models.city import City

            cities = storage.all(City)
            keys = cities.keys()
            temp = []
            for key in keys:
                if cities[key].state_id == self.id:
                    temp.append(cities[key])
            return temp
    
