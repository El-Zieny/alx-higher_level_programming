#!/usr/bin/python3
def add_tuple(a=(), b=()):

#    if not len(a):
#        return b
#    if not len(b):
#        return a
    if len(a) == 1 and len(b) == 1:
        return (a[0] + b[0], 0)
    if len(a) == 1 and len(b) == 2:
        return (a[0] + b[0], b[1])
    if len(a) == 2 and len(b) == 1:
        return (a[0] + b[0], a[1])
    x = a[0] + b[0]
    y = a[1] + b[1]
    return (x, y)
