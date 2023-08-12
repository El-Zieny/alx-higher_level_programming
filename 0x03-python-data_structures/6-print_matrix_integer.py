#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
        return
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            print("{}".format(matrix[x][y]), end="")
            if y != len(matrix[x]) - 1:
                print(" ", end="")
        print("")
