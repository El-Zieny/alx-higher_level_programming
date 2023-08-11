#!/usr/bin/python3
from sys import argv
if __name__ == "__main__"
    x = len(argv)
    if x == 2:
        print("1 argument:")
    elif x == 1:
        print("0 arguments.")
    elif x > 2:
        print("{} arguments:".format(x - 1))
    for c in range(1, x):
        print("{}: {}".format(c, argv[c]))
