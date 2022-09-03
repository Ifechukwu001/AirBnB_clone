#!/usr/bin/python3
""" Module containing the User class
"""
from .base_model import BaseModel


class User(BaseModel):
    """ User class

    Attributes:
        email (str):
        password (str):
        first_name (str):
        last_name (str):

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
