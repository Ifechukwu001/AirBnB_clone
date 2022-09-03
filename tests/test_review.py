#!/usr/bin/python3
"""test module for state.py"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class Teststate(unittest.TestCase):
    def test_class(self):
        """Test case to show that it is from the class State"""
        state = Review()
        self.AssertEqual(state.__class__.__name__, "Review")

    def test_superclass(self):
        """Test to show that State is a superclass of BaseModel"""
        state = Review()
        self.AssertTrue(issubclass(state.__class__.__name__, BaseModel)
