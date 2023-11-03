#!/usr/bin/python3
'''
Module: '0-nqueens'
'''

import sys


def place_queens(n, row, safe_queen_positions):
    """
    Parameters: n is an int that sets
                board size and # of queens
                row is row that we consider currently
    Prints: All possible solutions to placement
            (safe_queen_positions)
    """
    for col in range(n):
        is_safe = True
        for position in safe_queen_positions:
            # Check for column
            if col == position[1]:
                is_safe = False
                break
            # Check for positive diagonal
            if row - position[0] == col - position[1]:
                is_safe = False
                break
            # check for negative diagonal
            if position[0] - row == col - position[1]:
                is_safe = False
                break

        if is_safe:
            safe_queen_positions.append([row, col])
            if row != n - 1:
                place_queens(n, row + 1, safe_queen_positions)
            else:
                print(safe_queen_positions)
            del safe_queen_positions[-1]


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    place_queens(n, row=0, safe_queen_positions=[])


if __name__ == '__main__':
    main()
