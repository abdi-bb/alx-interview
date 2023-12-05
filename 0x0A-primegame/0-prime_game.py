#!/usr/bin/python3
'''
Module: '0-prime_game'
'''


def isPrime(num):
    '''
    Returns bool to indicate prime or not
    '''
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    '''
    From Ben and Maria, assuming Maria always goes first,
    return who the winner is
    '''
    maria_score = 0
    ben_score = 0
    num_of_rounds = 0

    while num_of_rounds <= x:
        for n in nums:
            prime_num_in_a_round = sum(
                1 for i in range(1, n + 1) if isPrime(i))

            # If the count of prime_num_in_a_round is odd, Maria wins;
            # otherwise, Ben wins
            if prime_num_in_a_round % 2 != 0:
                maria_score += 1
            else:
                ben_score += 1
        num_of_rounds += 1

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None
