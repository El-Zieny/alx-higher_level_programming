#!/usr/bin/python3
""" Square class that validate size"""


class Square:
    """Square class"""
    def __init__(self, s=0):
        """class constructor"""
        if type(s) is not int:
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
            self.__size = s
