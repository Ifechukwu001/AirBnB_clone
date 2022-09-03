#!/usr/bin/python3
"""test module for state.py"""

from models.base_model import BaseModel
from models.city import City
import unittest


class Teststate(unittest.TestCase):
    def test_class(self):
        """Test case to show that it is from the class State"""
        city = City()
        self.AssertEqual(city.__class__.__name__, "City")

    def test_superclass(self):
        """Test to show that State is a superclass of BaseModel"""
        city = City()
        self.AssertTrue(issubclass(city.__class__.__name__, BaseModel)
