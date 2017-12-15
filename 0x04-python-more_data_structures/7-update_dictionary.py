#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    new_dict = dict(my_dict)
    if key in new_dict:
        new_dict[key] = value
    else:
        new_dict.update({key : value})
    return new_dict
