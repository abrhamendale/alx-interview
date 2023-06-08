#!/usr/bin/python3
"""
Rotates a matrix.
"""


def rotate_2d_matrix(matrix):
    """
    A function to rotate a matrix.
    """
    ln = len(matrix)
    r_m = []
    rot_m = []
    for i in range(ln):
        for j in range(ln):
            r_m.append(matrix[j][i])
        r_m.reverse()
        rot_m.append(r_m)
        r_m = []
    for n in range(ln):
        matrix.insert(0, rot_m[n])
        matrix.pop()
    matrix.reverse()
