#!/usr/bin/python3
"""rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, w, h, x=0, y=0, ide=None):
        """Rectangle class constructor"""
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(ide)

    @property
    def width(self):
        """width of rectangle getter"""
        return self.__width

    @width.setter
    def width(self, w):
        """width setter"""
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, h):
        """height setter"""
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, v):
        """x setter"""
        if type(v) is not int:
            raise TypeError("x must be an integer")
        if v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, v):
        """y setter"""
        if type(v) is not int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v

    def area(self):
        """area getter"""
        area = self.__width * self.__height
        return area

    def display(self):
        """a function that displays a rectangle in #'s"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overwritting the str func"""
        name = f"[{self.__class__.__name__}] "
        ide = f"({self.id}) "
        x_y = f"{self.__x}/{self.__y} "
        sep = "- "
        w_h = f"{self.__width}/{self.__height}"

        return name + ide + x_y + sep + w_h

    def update(self, *args, **kwargs):
        """updating an existing rectangle"""
        if args is not None and len(args) > 0:
            attname = ['id', 'width', 'height', 'x', 'y']
            for attname, arg in zip(attname, args):
                setattr(self, attname, arg)
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary represintation of an instance"""
        dict_rep = {}
        attributes = ['id', 'width', 'height', 'x', 'y']
        for item in attributes:
            dict_rep[item] = getattr(self, item)

        return dict_rep
