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
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
