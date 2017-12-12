#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nt = [0, 0]

    for i in range(len(tuple_a)):
        nt[i] += tuple_a[i]
    for i in range(len(tuple_b)):
        nt[i] += tuple_b[i]

    return (nt[0], nt[1])
