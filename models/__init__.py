#!/usr/bin/python3
""" Module containing the models
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
__all__ = ["storage"]
