#!/usr/bin/python3
"""test module for state.py"""

from models.base_model import BaseModel
from models.place import Place
import unittest


class Teststate(unittest.TestCase):
    def test_class(self):
        """Test case to show that it is from the class State"""
        state = Place()
        self.AssertEqual(state.__class__.__name__, "Place")

    def test_superclass(self):
        """Test to show that State is a superclass of BaseModel"""
        state = Place()
        self.AssertTrue(issubclass(state.__class__.__name__, BaseModel)
