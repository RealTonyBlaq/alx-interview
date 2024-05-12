#!/usr/bin/python3
""" Interview prep """

from typing import List


def generate_factors(n: int) -> List[int]:
    """ Generates a list of factors from 2 to n """
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

    return unique()


def minOperations(n: int) -> int:
    """
    Returns an integer
    If n is impossible to achieve, returns 0.
    """
    factors, ops = generate_factors(n), []
    while n > 1:
        for i in factors:
            if n % i == 0:
                ops.append(i)
                n /= i
                break

    return sum(ops)
