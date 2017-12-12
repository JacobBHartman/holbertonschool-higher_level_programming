#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    nt = [0, 0]

    for i in range(min(len(tuple_a), 2)):
        nt[i] += tuple_a[i]
    for i in range(min(len(tuple_b), 2)):
        nt[i] += tuple_b[i]

    return (nt[0], nt[1])
