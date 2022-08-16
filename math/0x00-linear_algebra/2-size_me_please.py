#!/usr/bin/env python3
""" This module is used to calculate the shape of any given matrix """


def matrix_shape(matrix):
    """This Function calculates the shape of a matrix
Arguments:
matrix: Matrix to calculate shape
return -> Shape of matrix ([int,])
    """

    if (len(matrix) == 0):
        return([])
    shape = [len(matrix)]
    vector = matrix[0]
    while type(vector[0]) != int:
        shape.append(len(vector))
        vector = vector[0]
    shape.append(len(vector))
    return(shape)

if __name__ == "__name__":
    main()