#!/usr/bin/python3
'''
Module: '0-prime_game'
'''


def isPrime(n):
    '''helper func'''
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    '''main func'''
    maria_win, ben_win = 0, 0
    for _, n in zip(range(x), nums):
        primes_count = sum(1 for i in range(1, n + 1) if isPrime(i))
        ben_win += primes_count % 2 == 0
        maria_win += primes_count % 2 == 1
    if maria_win == ben_win:
        return None
    return 'Maria' if maria_win > ben_win else 'Ben'
