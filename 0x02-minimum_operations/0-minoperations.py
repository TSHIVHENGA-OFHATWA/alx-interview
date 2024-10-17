#!/usr/bin/python3
"""
This module defines the function minOperations that calculates
the minimum number of operations needed to result in exactly
n H characters in the file
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to result to result in
    exactly n H characters in the file

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required, or 0 if n is < 2.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
