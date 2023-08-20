#!/usr/bin/python3
for x in range(10):
    for i in range(10):
        if x != i and i > x:
            c = x * 10 + i
            if c != 89:
                print("{:02d}".format(c), end=", ")
            else:
                print("{:02d}".format(c))
