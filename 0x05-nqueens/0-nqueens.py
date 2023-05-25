#!/usr/bin/python3
"""
N queens in python
"""

import sys

queens = []
N = int(sys.argv[1])


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


def Nqueens(i_index, j_index, n, chess):
    """
    Calculates solutions for Nqueen.
    """
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (q_checker(i, j, N, chess) is False) and chess[i][j] != 1:
                chess[i + i_index][j + j_index] = 1
                queens.append([i, j])
                if Nqueens(0, 0, n - 1, chess) is True:
                    return True
                queens.pop()
                chess[i][j] = 0
    return False


if __name__ == '__main__':
    """Run main function."""
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    chess = [[0]*N for _ in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            Nqueens(i, j, N, chess)
    print(queens)
