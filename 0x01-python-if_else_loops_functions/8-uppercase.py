#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        value = ord(str[i])
        if value >= 97 and value <= 122:
            value -= 32
        print(chr(value), end="")
    print()
