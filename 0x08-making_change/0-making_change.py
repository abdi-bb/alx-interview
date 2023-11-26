#!/usr/bin/python3
'''
Module: '0-making_change'
'''


def makeChange(coins, total):
    '''Returns numbers of coin to meet yhe given total'''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    len_coins = len(coins)
    num_coins = 0
    sum_coins = 0
    idx = 0
    while sum_coins < total and idx < len_coins:
        while coins[idx] <= total - sum_coins:
            sum_coins += coins[idx]
            num_coins += 1
            if sum_coins == total:
                return num_coins
        i += 1
    return -1
