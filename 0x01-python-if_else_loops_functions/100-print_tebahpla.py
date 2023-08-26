#!/usr/bin/python3
for x in range(26, 0, -1):
    if x % 2:
        print(chr(x + 64), end="")
    else:
        print(chr(x + 96), end="")
