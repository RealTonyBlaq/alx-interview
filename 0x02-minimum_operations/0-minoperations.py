#!/usr/bin/python3
""" Interview prep """

from typing import List


def generate_factors(n: int) -> List[int]:
    """ Generates the prime factors of n """
    factors = []
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)
    # Returns unique elements in the list by converting to a set
    return factors


def minOperations(n: int) -> int:
    """
    Returns an integer
    If n is impossible to achieve, returns 0.
    """
    if n <= 1:
        return 0

    return sum(generate_factors(n))
