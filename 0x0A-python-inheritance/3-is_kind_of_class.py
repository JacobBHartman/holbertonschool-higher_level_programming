#!/usr/bin/python3
"""this module contains a function that reutnrs True if the object is an
instance of, or if the object is an instnce of a class that inherited from,
the specified class; otherwise False"""

def is_kind_of_class(obj, a_class):
    """this function returns True if the object is an
    instance of, or if the object is an instnce of a class that inherited from,
    the specified class; otherwise False"""

    return (isinstance(obj, a_class))
