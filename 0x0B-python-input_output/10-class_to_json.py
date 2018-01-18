#!/usr/bin/python3
"""
    contains a function that returns the dictionary description with simple
    data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
"""


def class_to_json(obj):
    """
        a function described by the module
    """
    return(vars(obj))
