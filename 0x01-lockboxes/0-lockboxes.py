#!/usr/bin/python3
'''
Module: '0-lockboxes'
'''

from typing import List


def canUnlockAll(boxes):
    ''''
    Determines if all the boxes can be opened.
    '''
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box (box 0)

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        # Check the keys in the current box
        for key in boxes[current_box]:
            if not visited[key]:
                stack.append(key)

    # If all boxes have been visited, return True, otherwise return False
    return all(visited)
