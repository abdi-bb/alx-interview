#!/usr/bin/python3
'''
Module: '0-making_change'
'''


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize an array to store
    # the minimum number of coins needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins needed to make change for total = 0

    for coin in coins:
        for value in range(coin, total + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
