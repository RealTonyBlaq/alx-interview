#!/usr/bin/env python3
""" A program that solves the N queens problem """

import sys

import sys

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    def solve(row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * N
    solve(0)
    return solutions

def print_solutions(solutions):
    for sol in solutions:
        formatted_solution = []
        for row, col in enumerate(sol):
            formatted_solution.append([row, col])
        print(formatted_solution)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
