#!/usr/bin/python3
"""
    this module contains a function that writes an Object to a text file
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
        this functions writes an Object to a text file using a JSON
        representation
    """
    import json
    json_obj = json.dumps(my_obj)
    with open(filename, mode='a', encoding='utf-8') as json_file:
        json_file.write(json_obj)
