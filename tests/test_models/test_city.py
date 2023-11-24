#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os


class test_City(test_basemodel):
    """ tests for city """

    def __init__(self, *args, **kwargs):
        """ inits the class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testing the state id method"""
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    def test_name(self):
        """ test name type"""
        new = self.value()
        self.assertEqual(type(new.name), str if
            os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))
