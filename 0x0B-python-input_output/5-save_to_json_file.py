#!/usr/bin/python3
"""A task to show the how to save an object to a json file"""
import json

def save_to_json_file(my_obj, filename):
    """A function that saves object to a json file
    Args:
        my_obj: object to be saved to file
        filename: The file to save to json"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dumps(my_obj)
