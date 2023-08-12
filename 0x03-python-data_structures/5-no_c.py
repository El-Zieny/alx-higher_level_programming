#!/usr/bin/python3
def no_c(string):
    new = ''
    for x in range(0, len(string)):
        if string[x] != "c" and string[x] != "C":
            new += string[x]
    return new
