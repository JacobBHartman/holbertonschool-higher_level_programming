#!/usr/bin/python3
"""this module contains a function that reutnrs True
if the object is an instnce of a class that inherited from,
the specified class; otherwise False"""

def inherits_from(obj, a_class):
    """this module contains a function that reutnrs True
    if the object is an instnce of a class that inherited from,
    the specified class; otherwise False"""

    return (isinstance(obj, a_class) and type(obj) is not a_class)
