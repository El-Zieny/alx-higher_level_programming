#!/usr/bin/python3
"""to json module"""


def to_json_string(my_obj):
    """to json string func"""
    from json import dumps
    return dumps(my_obj)
