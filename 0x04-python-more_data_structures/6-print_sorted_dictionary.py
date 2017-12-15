#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    new_dict = sorted(my_dict.items())
    for i, j in new_dict:
        print("{:s}: {:}".format(i, j))
