#!/usr/bin/env python3
""" A program that solves the N queens problem """

import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    N = int(sys.argv[1])
    
