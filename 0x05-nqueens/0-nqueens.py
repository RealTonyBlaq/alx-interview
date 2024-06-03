#!/usr/bin/env python3
""" A program that solves the N queens problem """

import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print('N must be at least 4')
        exit(1)
except ValueError:
    print('N must be a number')
    exit(1)

queen = []
