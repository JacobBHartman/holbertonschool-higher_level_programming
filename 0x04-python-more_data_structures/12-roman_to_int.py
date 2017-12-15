#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or (not isinstance(roman_string, str)):
        return 0

    sum = 0
    rs = roman_string[:]
    dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lng = len(roman_string)
    f1 = 0

    i = 0
    while i < lng:
        if i < lng - 1:
            if dct[rs[i+1]] > dct[rs[i]]:
                sum += dct[rs[i+1]] - dct[rs[i]]
                i += 1
                if rs[i] == 'I' and (rs[i+1] == 'X' or rs[i+1] == 'V'):
                    f1 = 1
            else:
                sum += dct[rs[i]]
        else:
            if f1 != 1:
                sum += dct[rs[i]]
        i += 1

    return sum
