#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    res = 0
    for c in range(1, x):
        res += int(argv[c])
    print(res)
