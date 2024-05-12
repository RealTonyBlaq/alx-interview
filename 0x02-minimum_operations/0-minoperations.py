#!/usr/bin/python3
""" Interview prep """

def minOperations(n: int) -> int:
    """
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    H, ops = 1, 0
    while H < n:
        copy, paste = H, H + copy
        ops += 2
        H = pa

    return ops
