#!/usr/bin/python3
"""function to add attribute to obj if possible"""


def add_attribute(obj, attr, value):
    if hasattr(obj, "__dict__") == False:
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, value)
