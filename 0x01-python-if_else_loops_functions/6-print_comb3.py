#!/usr/bin/python3
for i in range(89):
    first = i / 10
    second = i % 10
    if second > first:
        print("{:02d}, ".format(i), end="")
print("89")
