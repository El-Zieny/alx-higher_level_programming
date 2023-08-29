#!/usr/bin/python3
"""Square class size and area"""


class Square:
    """Square class"""

    def __init__(self, s=0):
        """class constructor"""
        if type(s) is not int:
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s
    def area(self):
        return self.__size ** 2
