#!/usr/bin/python3
"""
Module that contains the function `minOperations` which calculates the
fewest number of operations required to reach a specific number of 'H'
characters in a file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to get exactly `n`
    'H' characters in a file starting from a single 'H', given that the
    operations allowed are 'Copy All' and 'Paste'.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed to achieve exactly `n`
         characters. Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        # If n is 1 or less, it's impossible to have a valid solution.
        return 0

    operations = 0
    current = 1
    clipboard = 0

    # Loop until we reach the target number of characters (n)
    while current < n:
        # If n is divisible by the current number of characters, we can
        # do a "Copy All" followed by multiple "Paste" operations.
        if n % current == 0:
            clipboard = current
            operations += 1

        current += clipboard
        operations += 1

    return operations
