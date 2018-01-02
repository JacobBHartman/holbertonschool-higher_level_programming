#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j= 0;
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            j += 1
    except (TypeError, IndexError):
        pass
    print()
    return j
