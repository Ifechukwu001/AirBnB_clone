#!/usr/bin/python3
"""A file that contains the BaseModel class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """ init method.

        Args:
            args (:obj:`tuple`): Not used.
            kwargs (:obj:`dict`): Keyword arguments for initializing an object.

        Attributes:
            id (str): Unique identification of the object.
            created_at (:obj:`datetime.datetime`): Date_time object was created
            updated_at (:obj:`datetime.datetime`): Date_time object was updated

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                self.__setattr__(key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ str method.

        Returns:
            str: String representation of the object.

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) ({})".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Save method.

        Updates the attribute 'updated_at'

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Gets a dictionary representation of the object.

        Returns:
            :obj:`dict`: Dictionary represntation.

        """
        class_name = self.__class__.__name__
        new_dict = self.__dict__.copy()
        new_dict.update(__class__=class_name)
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())
        return new_dict
