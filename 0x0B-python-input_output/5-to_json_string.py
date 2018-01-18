#!/usr/bin/python3
"""
    this module contains a function that returns the JSON representation of an
    object (string)
"""


def to_json_string(my_obj):
    """
        this functions returns the JSON representation of an object (string
    """
    import json
    json_str = json.dumps(my_obj)
    return json_str
