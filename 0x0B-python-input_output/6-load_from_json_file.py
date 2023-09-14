#!/usr/bin/python3
"""load from json file module"""


def load_from_json_file(filename):
    """load from json file func"""
    with open(filename) as f:
        from json import load
        x = load(f)

    return x
