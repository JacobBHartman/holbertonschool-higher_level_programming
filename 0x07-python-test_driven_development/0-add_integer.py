#!/usr/bin/python3
"""this module contains one functcion that adds two integers"""


def add_integer(a, b):
    """

    adds two integers

    Args:
        a (int): the first integer
        b (int): the second integer

    Returns:
        the sum of the two integer. Error out if unable

    Raises:
        TypeError: if 'a' or 'b' are not floats or integers

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
