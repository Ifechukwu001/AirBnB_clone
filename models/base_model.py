#!/usr/bin/python3
"""A file that contains the BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class"""

    def __init__(self, name="", my_number=""):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) ({})" .format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        class_name = self.__class__.__name__
        new_dict = self.__dict__
        new_dict.update(__class__=class_name)
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())
        return new_dict
