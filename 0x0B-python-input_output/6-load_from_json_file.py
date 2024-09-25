#!/usr/bin/python3
"""A task to show the how to load an object from json file"""
import json


def load_from_json_file(filename):
    """A function that loads object to a json file
    Args:
        filename: The file to load json from"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
