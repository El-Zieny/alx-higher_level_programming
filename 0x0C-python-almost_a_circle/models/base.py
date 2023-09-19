#!/usr/bin/python3
"""base class module"""
from json import dumps, loads


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, ide=None):
        """class constructor"""
        if ide is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = ide

    @staticmethod
    def to_json_string(list_dict):
        """from list dictionary to json string"""
        if list_dict is not None and len(list_dict) > 0:
            return dumps(list_dict)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        lst = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for instance in list_objs:
                lst.append(cls.to_dictionary(instance))

        with open(filename, mode="w") as file:
            file.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        if json_string is not None:
            return loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """creates a new obj"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name + ".json", "r") as file:
                lst = cls.from_json_string(file.read())
                inst = []
                for item in lst:
                    inst.append(cls.create(**item))
                return inst
        except FileNotFoundError:
            return []

