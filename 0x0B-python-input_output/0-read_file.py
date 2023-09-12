#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """
    function to print the content of a filename to stdout
    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        print(file.read(), end="")
