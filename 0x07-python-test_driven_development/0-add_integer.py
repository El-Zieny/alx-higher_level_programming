#!/usr/bin/python3
"""
add two integers module
if error accure raise it
if a or b it's int casted
"""


def add_integer(a, b=98):
    """adds integers
    return a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    c = a + b

    return c
