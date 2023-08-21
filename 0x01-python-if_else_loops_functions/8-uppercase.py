#!/usr/bin/python3
def uppercase(str):
    strl = len(str)
    for c in range(strl):
        x = ord(str[c])
        if x > 96 and x < 123:
            print("{}".format(chr(x - 32)), end="")
        else:
            print("{}".format(chr(x)), end="")
    print("")
