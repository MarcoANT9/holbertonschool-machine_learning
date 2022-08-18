#!/usr/bin/env python3
"""This module flips matrixes arround"""


def matrix_transpose(matrix):
    """Function used to transpose a matrix
    Arguments:
        matrix: Matrix to traspose, it's never empty
    Return -> Transposed matrix"""

    if len(matrix) == 1:
        return matrix

    x_dimesion = len(matrix)
    y_dimesion = len(matrix[0])
    matrix2 = [[0 for x in range(x_dimesion)] for y in range(y_dimesion)]
    i = 0
    while i < len(matrix):
        j = 0
        vector = []
        while j < len(matrix[i]):
            matrix2[j][i] = matrix[i][j]
            j += 1
        i += 1

    return matrix2
