#!/usr/bin/python3
"""
Module: 0-making_change
This module provides a function to determine the minimum number of coins needed 
to meet a given total using coins of specified denominations.

The algorithm ensures an optimal solution by leveraging a greedy approach 
and considers edge cases such as when the total is zero or negative.
"""
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: Fewest number of coins needed to meet total or -1 if cannot.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
