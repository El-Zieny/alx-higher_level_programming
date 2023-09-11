#!/usr/bin/python3
"""my_int module"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
