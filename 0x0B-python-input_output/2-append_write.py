#!/usr/bin/python3
"""append to file module"""


def append_write(filename="", text=""):
    """function to append text to file"""
    with open(filename, mode="a", encoding="utf-8") as a:
        print(text, file=a, end="")

        return len(text)
