#!/usr/bin/python3
"""module"""


def is_kind_of_class(obj, a_class):
    """
    check if this obj is of 1_class or of a class inherites from that class
    """
    x = type(obj)

    return x == a_class or issubclass(x, a_class)
