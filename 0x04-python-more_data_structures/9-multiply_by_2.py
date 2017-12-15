#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = dict(my_dict)
    for j in new_dict:
        new_dict[j] *= 2
    return new_dict
