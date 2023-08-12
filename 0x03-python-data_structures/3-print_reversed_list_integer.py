#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    z = len(my_list) - 1
    for x in range(0, len(my_list)):
        print("{:d}".format(my_list[z]))
        z -= 1
