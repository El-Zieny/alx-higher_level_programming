#!/usr/bin/python3
"""
list sorting module
"""


class MyList(list):
    """
    inherits from list objext
    """

    def print_sorted(self):
        """
        returns the list sorted
        """
        print(sorted(self))
