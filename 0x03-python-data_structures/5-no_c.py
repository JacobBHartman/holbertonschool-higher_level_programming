#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    lng = len(new_string)
    i = 0
    while i < lng:
        if new_string[i] is 'c' or new_string[i] is 'C':
            del new_string[i]
            lng -= 1
        i += 1
    new_list = ''.join(new_string)
    return new_list
