#!/usr/bin/python3
""" Interview prep """

from typing import List


def generate_factors(n: int) -> List[int]:
    """ Generates a list of factors from 2 to n """
    prime_factors = [[] for _ in range(n+1)]
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
                prime_factors[i].append(p)
        p += 1

    for num in range(2, n+1):
        if primes[num]:
            prime_factors[num].append(num)

    return prime_factors
        

def minOperations(n: int) -> int:
    """
    Returns an integer
    If n is impossible to achieve, returns 0.
    """
    factors, ops = [2, 3, 5, 7, 11, 13, 17], []
    while n > 1:
        for i in factors:
            if n % i == 0:
                ops.append(i)
                n /= i
                break

    return sum(ops)
