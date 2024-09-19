#!/usr/bin/python3
"""A function that returns an object from a JSON file"""
import json


def from_json_string(my_str):
    """ a function that returns an object from json
    Arg:
        my_obj: the object to be stringified
    """
    return json.loads(my_str)
