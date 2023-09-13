#!/usr/bin/python3
"""from json string module"""


def from_json_string(my_str):
    """from json string func"""
    from json import loads
    return loads(my_str)
