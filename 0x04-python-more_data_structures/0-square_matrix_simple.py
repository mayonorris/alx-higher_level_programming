#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  sq_matrix = ([list(map(lambda elt: elt**2, row)) for row in matrix])
  return (sq_matrix)
