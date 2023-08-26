#!/usr/bin/python3
for x in range(26, 0, -1):
        print("{}".format(chr(x + 64 if x % 2 else x + 96)), end="")
