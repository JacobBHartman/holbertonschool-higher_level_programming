#!/usr/bin/python3
"""
    this module contains a function that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
        this function writes a string to a text file (UTF8) and returns the
        number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    with open(filename, encoding='utf-8') as f:
        chars_wrote = 0
        for line in f:
            for chrs in line:
                chars_wrote += 1
    return chars_wrote
