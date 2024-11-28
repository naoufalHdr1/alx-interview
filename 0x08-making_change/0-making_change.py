#!/usr/bin/python3
"""
Module: 0-making_change

This module contains a function to determine the minimum number of coins
required to meet a given total using a list of coin denominations.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Parameters:
    - coins (list): A list of integers representing the coin denominations.
    - total (int): The total amount to be made with the coins.

    Returns:
    - int: The minimum number of coins needed to meet the total.
           If the total is 0 or less, returns 0.
           If the total cannot be met with the given coins, returns -1.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for greedy approach
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    # If total is not 0, we couldn't meet the exact amount
    return count if total == 0 else -1
