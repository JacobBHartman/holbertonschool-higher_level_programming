#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = [0, '']
    if sentence is "":
        return (0, None)
    tuple[1] = sentence[0]
    tuple[0] = len(sentence)
    return (tuple[0], tuple[1])
