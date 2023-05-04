#!/usr/bin/python3
"""
Minimum operations
"""


def helper(cp, cpv, check, num, h, n):
    """Helper function."""
    ret1 = 0
    ret2 = 0
    if cp == 0:
        h = h + cpv
        num = num + 1
    else:
        if cpv < h:
            num = num + 1
        cpv = h
    if h == n:
        if num <= check:
            check = num
        return (check)

    if h < n:
        ret1 = helper(0, cpv, check, num, h, n)
        if cpv < h:
            ret2 = helper(1, cpv, check, num, h, n)
            if ret1 < ret2:
                return (ret1)
            else:
                return (ret2)
        return (ret1)
    else:
        return (h)


def minOperations(n):
    """Computes the minimum number of operations required."""
    cp = 1
    cpv = 0
    check = n
    num = 0
    h = 1
    ret1 = 0
    ret2 = 0

    if n <= 1:
        return (0)
    if n == 2:
        return (2)
    cpv = 1
    num = 2
    h = 2

    print("cp", cp, "cpv", cpv, "num", num, "h", h, "check", check)

    ret1 = helper(0, cpv, check, num, h, n)
    if cpv < h:
        ret2 = helper(1, cpv, check, num, h, n)

        if ret1 < ret2:
            return (ret1)
        else:
            return (ret2)
    return (ret1)
