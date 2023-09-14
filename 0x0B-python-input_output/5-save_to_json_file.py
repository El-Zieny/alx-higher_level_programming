#\!/usr/bin/python3
"""save object to file module"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file function"""
    with open(filename, "w") as j:
        from json import dump
        dump(my_obj, j)
