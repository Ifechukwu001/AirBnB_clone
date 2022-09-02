#!/usr/bin/python3
""" Module containing the class FileStorage.
"""
import json
from ..base_model import BaseModel

class FileStorage:
    """ FileStorage class.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the objects stored in the private dictionary.

        Returns:
            :obj:`dict`: Dictionary of the objects.

        """
        return __objects

    def new(self, obj):
        """ Adds a new object to the private dictionary.

        Args:
            obj (:obj:`*`): Object to be added.

        """
        obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        __objects[obj_id] = obj

    def save(self):
        """ Saves the private dictionary to a json file.

        """
        json_dict = {}
        for obj_id, obj in __objects.items():
            json_dict[obj_id] = obj.to_dict()
        with open(__file_path, mode="w", encoding="utf-8") as obj_file:
            json.dump(json_dict, obj_file)

    def reload(self):
        """ Loads the private dictionary from a json file.

        """
        try:
            with open(__file_path, encoding="utf-8") as obj_file:
                json_dict = json.load(obj_file)
        except:
            pass
        else:
            __objects = {}
            for obj_id, obj_dict in json_dict.items():
                obj = BaseModel(**obj_dict)
                __objects[obj_id] = obj