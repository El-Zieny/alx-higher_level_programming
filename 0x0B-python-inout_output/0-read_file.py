#!/usr/bin/python3
"""module to open, read, and writ the content of a file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read())
