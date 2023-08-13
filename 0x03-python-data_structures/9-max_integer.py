#!/usr/bin/python3
def max_integer(a=[]):
    if not a:
        return None
    z = a[0]
    for x in range(0, len(a)):
        if a[x] > z:
            z = a[x]
    return z
