#!/usr/bin/python3
"""All BaseModel unittest"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCode):
    """BaseModel unittest"""
    def test_id(self):
        """checks if id is unique"""
        id1 = BaseModel.id()
        id2 = BaseModel.id()
        self.assertNotEqual(id1, id2)
        self.assertisinstance(id1, str)

    def test_created_at(self):
        id1 = BaseModel()
        self.assertTrue(id1, "created_at")

    def test_updated_at(self):
        update = BaseModel()
        old_time = update.updated_at
        update.save
