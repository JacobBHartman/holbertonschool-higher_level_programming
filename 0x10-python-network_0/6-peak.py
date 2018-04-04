#!/usr/bin/python3
"""
    this module contains a function that finds a peak
"""


def find_peak(list_of_integers):
    """
        this method finds a peak in a list of unsorted integers
    """
    length_list = len(list_of_integers)
    if length_list > 2:
        for i in range(1, length_list - 1):
            if list_of_integers[i] > list_of_integers[i - 1]:
                if list_of_integers[i] > list_of_integers[i + 1]:
                    return list_of_integers[i]
    return None
