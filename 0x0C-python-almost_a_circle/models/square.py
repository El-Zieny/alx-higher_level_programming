#!/usr/bin/python3
"""square class module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, ide=None):
       super().__init__(size, size, x, y, ide)

    def __str__(self):
        name = f"[{self.__class__.__name__}] "
        ide = f"({self.id}) "
        x_y = f"{self.x}/{self.y} "
        sep = "- "
        size = f"{self.width}"

        return name + ide + x_y + sep + size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            keys = ['id', 'size', 'x', 'y']
            for key, arg in zip(keys, args):
                    setattr(self, key, arg)
        elif kwargs is not None and len(kwargs) > 0:
            for key, arg in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, arg)

    def to_dictionary(self):
        class_dict = {}
        attributes = ['id', 'size', 'x', 'y']
        for attribute in attributes:
            class_dict[attribute] = getattr(self, attribute)

        return class_dict
