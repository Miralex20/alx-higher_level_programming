#!/usr/bin/python3
"""A script that adds all arguments to a python
list and saves them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json.file

    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_items.json")
