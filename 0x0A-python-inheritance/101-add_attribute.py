#!/usr/bin/python3
"""module of a function to add attribute to obj if possible"""


def add_attribute(obj, attr, value):
    """function to add attribute to obj if possible"""
    if hasattr(obj, "__dict__") == False:
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, value)
