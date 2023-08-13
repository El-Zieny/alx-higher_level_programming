#!/usr/bin/python3
def delete_at(a=[], i=0):
    if i > len(a) or i < 0:
        return a
    a.pop(i)
    return a
