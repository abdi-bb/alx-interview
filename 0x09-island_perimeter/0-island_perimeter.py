#!/usr/bin/python3
'''
Module: '0-island_perimeter'
Calculates perimeter of island
'''


def island_perimeter(grid):
    '''
    Returns perimeter of island
    '''
    perimeter = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                perimeter += 4

                # Check top neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check left neighbour
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
