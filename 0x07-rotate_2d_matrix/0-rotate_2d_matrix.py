#!/usr/bin/python3
""" Rotate a 2D Matrix """

def rotate_2d_matrix(matrix):
    """ Rotates an n x n Matrix 90 degrees clockwise """
    n = len(matrix)
    for r in range(n, 0, ):
        for c in range(n):
            temp = matrix[r][c]
