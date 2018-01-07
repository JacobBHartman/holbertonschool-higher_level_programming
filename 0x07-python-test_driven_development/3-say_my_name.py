#!/usr/bin/python3
"""this module prints a persons full name"""

def say_my_name(first_name, last_name=""):
    """
    prints 'My Name Is'

    Args:
        first_name (str): a persons first name
        last_name  (str): a persons last name

    Returns:
        nothing

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
