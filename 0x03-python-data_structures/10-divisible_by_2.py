#!/usr/bin/python3
def divisible_by_2(a=[]):
    b = list()
    for x in range(0, len(a)):
        if a[x] % 2:
            b.append(False)
        else:
            b.append(True)
    return b
