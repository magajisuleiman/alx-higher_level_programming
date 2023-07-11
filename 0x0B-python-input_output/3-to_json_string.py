#!/usr/bin/python3

"""
module 3-to_json_string.py

contains a function that returns the JSON rep of an obj
"""


def to_json_string(my_obj):
    """A function that returns the JSON rep of an obj"""
    import json

    return json.dumps(my_obj)
