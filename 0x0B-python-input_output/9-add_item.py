#!/usr/bin/python3
"""
    this module contains a script that adds all arguments to a Python list,
    and then save them to a file
"""


import json
from sys import argv
import os.path


def save_to_json_file(my_obj, filename):
    """
        this functions writes an Object to a text file using a JSON
        representation
    """
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)


def load_from_json_file(filename):
    """
        this function creates an Object from a "JSON file"
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    filename = "add_item.json"

    my_obj = []
    if os.path.isfile(filename):
        my_obj = load_from_json_file(filename)
    for i in range(1, len(argv)):
        my_obj.append(argv[i])

    save_to_json_file(my_obj, filename)
