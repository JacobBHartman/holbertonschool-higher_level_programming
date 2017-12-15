#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    largest = 0
    name = ""
    new_dict = dict(my_dict)
    for i, j in new_dict.items():
        if j > largest:
            largest = j
            name = i
    return name
