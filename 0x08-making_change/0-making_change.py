#!/usr/bin/python3
'''
Module: '0-making_change'
'''


def makeChange(coins, total):
    '''Returns numbers of coin to meet yhe given total'''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    sum = 0
    i = 0
    num_coins = 0
    len_coins = len(coins)
    while sum < total and i < len_coins:
        while coins[i] <= total - sum:
            sum += coins[i]
            num_coins += 1
            if sum == total:
                return num_coins
        i += 1
    return -1
