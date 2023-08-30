#!/usr/bin/python3
"""class file"""


class Square:
    """Square class"""

    def __init__(self, s, po=(0, 0)):
    """class constructor"""
        if type(s) is not int:
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s
        if type(po) is not tuple or len(po) != 2 or \
                type(po[0]) is not int or type(po[1]) is not int or \
                po[0] < 0 or po[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self._position = po

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, s):
        if type(s) is not int:
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, p):
        if type(p) is not tuple or len(p) != 2 \
        or type(p[0]) is not int or type(p[1]) is not int \
        or p[0] < 0 or p[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self._position = p



    def my_print(self):
        if self.__size == 0:
            print()
            return
        for a in range(self._position[1]):
            print()
        for x in range(self.__size):
            for b in range(self._position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print()
