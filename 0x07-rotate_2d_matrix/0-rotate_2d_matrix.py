#!/usr/bin/python3
'''
Module 0-rotate_2d_matrix
'''


def rotate_2d_matrix(matrix):
    '''
    Rotates a 2D matrix
    90 Degree clockwise
    '''
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
