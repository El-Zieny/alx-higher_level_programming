#!/usr/bin/python3
""" Square class that validate size"""


class Square:
    """Square class"""
    def __init__(self, s=0):
        try:
            self.size = s
        except TypeError:
            print("size must be an integer")
        except s < 0:
            print("size must be >= 0")
