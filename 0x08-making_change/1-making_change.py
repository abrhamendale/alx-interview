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
    #print(max_weight, arr[ind])
    for i in range(max_weight, -1, -1):
        #print(val_arr)
        itot = tot - i * arr[ind]
        val_arr[ind] = i
        if ind < len(arr) - 1:
            if change_helper(arr, val_arr, total, ind + 1, itot):
                return True
        if multiplier(val_arr, arr) == total:
            return True


"""
    while multiplier(val_arr, arr) <= tot:
        if ind == len(val_arr):
            break
        if sum(val_arr) <= sum(opt_arr) and multiplier(val_arr, arr) == tot:
            for i in range(len(arr)):
                opt_arr[i] = val_arr[i]
        if ind < len(val_arr):
            ind = ind + 1
            change_helper(arr, val_arr, opt_arr, ind, tot)
            if ind < len(val_arr):
                val_arr[ind] = 0
            ind = ind - 1
        val_arr[ind] = val_arr[ind] + 1
"""

def makeChange(coins, total):
    """
    Calculates the smallest sets of
    changes that equals a total.
    """
    if total <= 0:
        return 0
    val_arr = []
    opt_arr = []
    for i in range(len(coins)):
        val_arr.append(0)
        opt_arr.append(max(coins))
    ind = 0
    fail_sm = sum(opt_arr)
    t_0 = timeit.default_timer()
    if change_helper(sorted(coins, reverse = True), val_arr, total, ind, total):
        t_1 = timeit.default_timer()
        print(round((t_1 - t_0) * 10 ** 6, 3))
        return sum(val_arr)
    else:
        return -1
