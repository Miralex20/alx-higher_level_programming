#!/usr/bin/python3
"""A function that demonstrates the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ a function that performs the stringify task
    Arg:
        my_obj: the object to be stringified
    """
    return json.dumps(my_obj)
