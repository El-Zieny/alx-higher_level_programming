#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            z = 1
            break
        else:
            i += 1 
    print()
    return i
