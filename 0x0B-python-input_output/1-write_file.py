#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """a function that overwrite a file or create it if it doesnt exist"""
    with open(filename, mode="w", encoding="utf-8") as wr:
        x = wr.write(text)

    return x
