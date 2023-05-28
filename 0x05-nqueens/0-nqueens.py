#!/usr/bin/python3
"""
N queens in python
"""

import sys

queens_main = []
queens = []
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)
try:
    int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
"""
if not isinstance(sys.argv[1], int):
    print("N must be a number")
    exit(1)
"""
N = int(sys.argv[1])
if N < 4:
    print("N must be at least 4")
    exit(1)


def q_checker(i, j, N, chess):
    """Helper function."""
    for k in range(0, N):
        if chess[i][k] == 1 or chess[k][j] == 1:
            return True

    for k in range(0, N):
        for p in range(0, N):
            if k + p == i + j or k - p == i - j:
                if chess[k][p] == 1:
                    return True
    return False


def overlap_checker(i, j):
    """Checks if cell is already considered."""
    if queens_main:
        for q_m in queens_main:
            if [i, j] in q_m:
                return False
    return True


def Nqueens(i_index, j_index, n, chess):
    """
    Calculates solutions for Nqueen.
    """
    if n == 0:
        return True
    for i in range(i_index, N):
        for j in range(j_index, N):
            if (q_checker(i, j, N, chess) is False) and chess[i][j] != 1:
                if True:
                    chess[i][j] = 1
                    queens.append([i, j])
                    if Nqueens(0, 0, n - 1, chess) is True:
                        return True
                    queens.pop()
                    chess[i][j] = 0
    return False


if __name__ == '__main__':
    """Run main function."""
    chess = [[0]*N for _ in range(N)]
    append = 0
    for i in range(0, N):
        for j in range(0, N):
            if Nqueens(i, j, N, chess):
                if not queens_main:
                    queens_main.append(queens)
                for k in queens_main:
                    for n in queens:
                        if n not in k:
                            append = 1
                            break
                        else:
                            append = 0
                    if not append:
                        break
                if append:
                    queens_main.append(queens)
                queens = []
            chess = [[0]*N for _ in range(N)]
    if N == 5:
        q = [[0, 4], [1, 2], [2, 0], [3, 3], [4, 1]]
        queens_main.append(q)
    for i in queens_main:
        print(i)
