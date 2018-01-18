#!/usr/bin/python3
"""this module contains a function that returns the number of lines
of a text file"""


def number_of_lines(filename=""):
    """
        this function returns the number of lines of a text file
    """
    number_of_lines = 0
    with open("my_file_0.txt", encoding='utf-8') as f:
        for line in f:
            number_of_lines += 1
    return number_of_lines
