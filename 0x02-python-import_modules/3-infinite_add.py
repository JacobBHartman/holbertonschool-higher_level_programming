#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv) - 1
    sum = 0

    for i in range(n_args):
        sum += int(sys.argv[i + 1])
    print("{:d}".format(sum))
