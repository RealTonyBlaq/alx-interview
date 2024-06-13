#!/usr/bin/python3
""" Rotate a 2D Matrix """

def rotate_2d_matrix(matrix):
    """ Rotates an n x n Matrix 90 degrees clockwise """
    if matrix and type(matrix) is list:
        n = len(matrix)
        for i in range(n):
            for matris in matrix:
                new[i].append(matris[i])
            new[i].reverse()
