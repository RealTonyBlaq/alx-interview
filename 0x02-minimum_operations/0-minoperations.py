#!/usr/bin/python3
""" Interview prep """

def minOperations(n: int) -> int:
    """
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    H, ops, copy = 1, 0, 
    while H < n:
        if copy + H <= n:
            copy = H
        paste = H + copy
        ops += 2
        H = paste

    return ops
