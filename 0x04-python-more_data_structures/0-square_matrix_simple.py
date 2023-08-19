#!/usr/bin/python3
def square_matrix_Simple(matrix=[]):
    if not matrix
        return None
    new = []
    for row in matrix:
        new.append(list(map(lambda x: x**x, row)))
    return new
