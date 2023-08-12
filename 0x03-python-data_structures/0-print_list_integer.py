#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = len(my_list)
    for c in range(0, x):
        i = int(my_list[c])
        print("{}".format(i))
