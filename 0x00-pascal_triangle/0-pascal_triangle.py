#!/usr/bin/python3

'''
Module: pascal_triangle
'''


def pascal_triangle(n):
    '''Returns Pascal's Triangle'''
    if n <= 0:
        return []

    triangle = [[1]]

    for row in range(1, n):
        # number of row = n
        prev_row = triangle[-1]
        new_row = [1]

        for column in range(1, row):
            # number of column = number of row
            new_value = prev_row[column - 1] + prev_row[column]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
