#!/usr/bin/python3
""" init module of the models package

"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
__all__ = ["storage"]
