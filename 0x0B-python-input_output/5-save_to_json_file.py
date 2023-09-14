#\!/usr/bin/python3
"""save object to file module"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file function
    :return: string
    :rtype: str
    """
    with open(file=filename, mode='w') as j:
        from json import dump
        dump(my_obj, j)
