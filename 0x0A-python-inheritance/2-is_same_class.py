#!/usr/bin/python3
"""this module contains a function that returns True if the objects is exactly
an instance of the specified class, otherwise False"""

def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly an instance of
    the specified class, otherwise False"""

    return (type(obj) is a_class)
