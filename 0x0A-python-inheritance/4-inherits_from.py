#!/usr/bin/python3
"""module"""


def is_kind_of_class(obj, a_class):
    """
    an object of a class inheritanc
    """
    return issubclass(type(obj), a_class)
