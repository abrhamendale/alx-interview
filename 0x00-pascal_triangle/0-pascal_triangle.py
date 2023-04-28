#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n=5):
    """Returns pascals triangle in a list of lists format."""
    tr = []
    for i in range(n):
        tr.append(list())
        tr[i].append(1)
        if i > 1:
            for j in range(1, i):
                tr[i].append(tr[i - 1][j] + tr[i - 1][j - 1])
        if i > 0:
            tr[i].append(1)
    return (tr)
