#!/usr/bin/python3
"""test module for state.py"""

from models.base_model import BaseModel
from models.state import State
import unittest


class Teststate(unittest.TestCase):
    def test_class(self):
        """Test case to show that it is from the class State"""
        state = State()
        self.AssertEqual(state.__class__.__name__, "State")

    def test_superclass(self):
        """Test to show that State is a superclass of BaseModel"""
        state = State()
        self.AssertTrue(issubclass(state.__class__.__name__, "BaseModel")                
