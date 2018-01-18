#!/usr/bin/python3
"""
    this module contains a function that reads n lines of a text file (UTF8)
    and prints it to stdout
"""


def read_file(filename="", num_lin=0):
    """this function contains a function that reads a text file (UTF8)
    and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        i = 0
        for line in f:
            if i < num_lin:
                print(line, end="")
            i += 1


def number_of_lines(filename=""):
    """
        this function returns the number of lines of a text file
    """
    number_of_lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            number_of_lines += 1
    return number_of_lines


def read_lines(filename="", nb_lines=0):
    """
        this functions reads n lines of a textfile (UTF8) and prints it to
        stdout
    """
    if nb_lines <= 0 or nb_lines >= number_of_lines(filename):
        read_file(filename, number_of_lines(filename))
    else:
        read_file(filename, nb_lines)
