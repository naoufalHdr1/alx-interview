#!/usr/bin/python3
"""
Prime Game Module
This module defines a solution to the "Prime Game" problem
"""
from typing import List, Optional


def sieve_of_eratosthenes(n: int) -> List[bool]:
    """
    Computes prime numbers up to n using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The maximum number to check for primality.

    Returns:
        List[bool]: A boolean list where True indicates a prime number.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes


def count_primes_up_to(n: int, primes: List[bool]) -> int:
    """
    Counts the number of prime numbers up to n.

    Args:
        n (int): The upper limit.
        primes (List[bool]): The list indicating primality.

    Returns:
        int: The count of primes up to n.
    """
    return sum(primes[:n + 1])


def isWinner(x: int, nums: List[int]) -> Optional[str]:
    """
    Determines the winner of the Prime Game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of integers, one for each round.

    Returns:
        Optional[str]: "Maria" if Maria wins, "Ben" if Ben wins, or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)  # Find the largest number in nums
    primes = sieve_of_eratosthenes(max_num)  # Precompute primes up to max_num

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, primes)
        # Maria wins if the prime count is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
