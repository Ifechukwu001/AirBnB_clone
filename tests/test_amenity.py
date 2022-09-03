#!/usr/bin/python3
"""test module for state.py"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class Teststate(unittest.TestCase):
    def test_class(self):
        """Test case to show that it is from the class State"""
        state = Amenity()
        self.AssertEqual(state.__class__.__name__, "Amenity")

    def test_superclass(self):
        """Test to show that State is a superclass of BaseModel"""
        state = Amenity()
        self.AssertTrue(issubclass(state.__class__.__name__, BaseModel)
