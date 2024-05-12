#!/usr/bin/python3
""" Interview prep """


def generate_factors()

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
