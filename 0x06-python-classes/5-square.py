#!/usr/bin/python3
"""square class file"""


class Square:
    """Square class"""

    def __init__(self, s=0):
        if type(s) is not int:
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s

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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for z in range(self.__size):
                    print("#", end="")
                print()
