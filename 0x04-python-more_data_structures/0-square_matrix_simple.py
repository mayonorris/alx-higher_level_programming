#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = matrix.copy()
    sq_matrix = [list(map(lambda elt: elt**2, row)) for row in matrix]
    return (sq_matrix)
