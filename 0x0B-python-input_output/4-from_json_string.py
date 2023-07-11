#!/usr/bin/python3

"""
module 4-from_json_string.py

contain a function that return python objects
"""


def from_json_string(my_str):
    """A function that returns a python object"""
    import json

    return json.loads(my_str)
