#!/usr/bin/python3
"""
    function of matrix divided
"""


def matrix_divided(matrix, div):
    new_mat = []
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        new_mat1 = []
        c = len(matrix[0])
        if c != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in range(len(matrix[i])):
            if type (matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                new_mat1.append(round (matrix[i][j] / div, 2))
        new_mat.append(new_mat1)
    return(new_mat)

        