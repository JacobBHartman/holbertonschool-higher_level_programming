#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv) - 1

    if (n_args == 0):
        print("{:d} arguments.".format(n_args))
    elif (n_args == 1):
        print("{:d} argument:".format(n_args))
    else:
        print("{:d} arguments:".format(n_args))
    for i in range(n_args):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
