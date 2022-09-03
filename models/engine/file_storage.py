#!/usr/bin/python3
""" Module containing the class FileStorage.
"""
import json
from ..base_model import BaseModel


class FileStorage:
    """ FileStorage class.

    """
    __file_path = "./file.json"
    __objects = {}
    __classes = {"BaseModel": BaseModel}

    def all(self):
        """ Returns the objects stored in the private dictionary.

        Returns:
            :obj:`dict`: Dictionary of the objects.

        """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new object to the private dictionary.

        Args:
            obj (:obj:`*`): Object to be added.

        """
        obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """ Saves the private dictionary to a json file.

        """
        json_dict = {}
        for obj_id, obj in FileStorage.__objects.items():
            json_dict[obj_id] = obj.to_dict()
        file_path = FileStorage.__file_path
        with open(file_path, mode="w", encoding="utf-8") as obj_file:
            json.dump(json_dict, obj_file)

    def reload(self):
        """ Loads the private dictionary from a json file.

        """
        try:
            file_path = FileStorage.__file_path
            with open(file_path, encoding="utf-8") as obj_file:
                json_dict = json.load(obj_file)
        except Exception:
            pass
        else:
            FileStorage.__objects = {}
            for obj_id, obj_dict in json_dict.items():
                obj = FileStorage.__classes[obj_dict["__class__"]](**obj_dict)
                FileStorage.__objects[obj_id] = obj
