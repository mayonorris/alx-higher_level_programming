#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cp = matrix.copy()
    sq_matrix = ([list(map(lambda elt: elt**2, row)) for row in matrix_cp])
  return (sq_matrix)
