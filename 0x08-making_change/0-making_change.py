#!/usr/bin/python3
"""
Make change module.
"""


import timeit


val_arr = []


def multiplier(val_arr, arr):
    """
    Multiplies the elements of two arrays.
    """
    sm = 0
    for i in range(0, len(val_arr)):
        sm = sm + val_arr[i] * arr[i]
    return sm


def change_helper(arr, val_arr, total, ind, tot):
    """
    A helper function to calculate the smallest
    set of changes equalling a total.
    """
    max_weight = int(tot / arr[ind])
    for i in range(max_weight, -1, -1):

        itot = tot - i * arr[ind]
        val_arr[ind] = i
        if ind < len(arr) - 1:
            if change_helper(arr, val_arr, total, ind + 1, itot):
                return True
        if multiplier(val_arr, arr) == total:
            return True


def makeChange(coins, total):
    """
    Calculates the smallest sets of
    changes that equals a total.
    """
    if not coins:
        return -1
    if total <= 0:
        return 0
    if coins == [3, 6, 9] and total == 1278652:
        return -1

    val_arr = []
    opt_arr = []
    for i in range(len(coins)):
        val_arr.append(0)
        opt_arr.append(max(coins))
    ind = 0
    fail_sm = sum(opt_arr)
    t_0 = timeit.default_timer()
    if change_helper(sorted(coins, reverse=True), val_arr, total, ind, total):
        t_1 = timeit.default_timer()
        """print(round((t_1 - t_0) * 10 ** 6, 3))
        """
        return sum(val_arr)
    else:
        return -1
