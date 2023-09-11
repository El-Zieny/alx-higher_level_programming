#!/usr/bin/python3
"""list sorting module"""


class MyList(list):
    """
    inherits from list objext
    """

    def print_sorted(self):
        """
        prints the list sorted
        :return:
        :rtype:
        """
        print(sorted(self))
