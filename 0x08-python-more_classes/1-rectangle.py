#!/usr/bin/python3
"""rectangle module"""


class Rectangle:
    """rectangle class"""
    def __init__(self, w=0, h=0):
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w

    @property
    def width(self):
        return self.__height

    @height.setter
    def width(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if w < 0:
            raise ValueError("height must be >= 0")
        self.__height = h
