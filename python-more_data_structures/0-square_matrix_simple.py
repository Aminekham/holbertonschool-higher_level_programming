#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in range(len(matrix)):
        res0 = []
        for j in range(len(matrix[i])):
            res0.append(matrix[i][j] ** 2)
        res.append(res0)
    return(res)
