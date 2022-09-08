#!/usr/bin/python3
""" Unittests for BaseModel class
"""
from models.base_model import BaseModel
import unittest
import datetime

class TestBaseModel(unittest.TestCase):
    """ TestBaseModel class
    """
    def test_id_unique_string(self):
        """Checks if id is unique
        """
        one = BaseModel()
        two = BaseModel()
        three = BaseModel()
        self.assertNotEqual(one.id, two.id)
        self.assertNotEqual(two.id, three.id)
        self.assertNotEqual(three.id, one.id)
        self.assertTrue(type(one.id) is str)

    def test_check_datetime_variables(self):
        """Checks if the created_at and updated_at variables
        are datetime objects

        """
        one = BaseModel()
        self.assertTrue(type(one.created_at) is datetime.datetime)
        self.assertTrue(type(one.updated_at) is datetime.datetime)

    def test_save_method(self):
        """Checks if save method updates the update time"""
        one = BaseModel()
        updated = one.updated_at
        one.save()
        self.assertNotEqual(one.updated_at, updated)

    def test_str(self):
        """Checks for proper formatting of str"""
        one = BaseModel()
        self.assertEqual(str(one), "[{}] ({}) {}".format(
            one.__class__.__name__, one.id, one.__dict__))

    def test_to_dict(self):
        """Checks for the appropiate dicto=ionary returned"""
        one = BaseModel()
        to_dict = one.to_dict()
        for key in one.__dict__.keys():
            self.assertTrue(key in to_dict)
        self.assertTrue("__class__" in to_dict)
        self.assertTrue(type(to_dict["created_at"]) is str)
        self.assertTrue(type(to_dict["updated_at"]) is str)
