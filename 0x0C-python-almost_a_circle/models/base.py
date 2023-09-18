#!/usr/bin/python3
"""base lass module"""
from json import dumps, loads

class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, ide=None):
        if ide is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = ide

    @staticmethod
    def to_json_string(list_dict):
        if list_dict is not None and len(list_dict) > 0:
            return dumps(list_dict)
        else:
            return "[]"
