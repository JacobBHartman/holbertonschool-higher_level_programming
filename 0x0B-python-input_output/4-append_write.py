#!/usr/bin/python3
"""
    this module contains a function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
        this function appends a string at the end of a text file (UTF8) and
        returns the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
