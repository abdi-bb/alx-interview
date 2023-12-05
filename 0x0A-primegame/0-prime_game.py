#!/usr/bin/python3
'''
Module: '0-prime_game'
'''


def is_prime(n):
    '''helper func'''
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    '''main func'''
    maria = 0
    ben = 0
    for _ in range(x):
        for n in nums:
            numbers = list(range(1, n + 1))
            maria_turn = True
            while numbers:
                can_move = False
                for i in reversed(numbers):
                    if is_prime(i):
                        # Remove the number and its multiples from the list
                        numbers = [j for j in numbers if j % i != 0]
                        can_move = True
                        break
                if not can_move:
                    if maria_turn:
                        ben += 1
                    else:
                        maria += 1
                    break
                maria_turn = not maria_turn
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
