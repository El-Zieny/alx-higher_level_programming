#!/usr/bin/python3
"""Square class file"""


class Square:
    """Square class"""

    def __init__(self, s, po=(0, 0)):
        """class constructor"""
        if type(s) is not int:
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s
        if type(po) is not tuple or len(po) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(po[0]) is not int or type(po[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if po[0] < 0 or po[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = po

    def area(self):
        """square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, s):
        """"size setter"""
        if type(s) is not int:
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, p):
        """position setter"""
        if type(p) is not tuple or len(p) != 2: 
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(p[0]) is not int or type(p[1]) is not int:         
            raise TypeError('position must be a tuple of 2 positive integers')
        if p[0] < 0 or p[1] < 0:       
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = p

    def my_print(self):
        """print current square with # taking position"""
        if self.__size == 0:
            print()
            return
        for a in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for b in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print()
