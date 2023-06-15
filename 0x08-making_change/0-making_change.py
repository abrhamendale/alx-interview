#!/usr/bin/python3
"""
Make change module.
"""

opt_arr = []


def multiplier(val_arr, arr):
    """
    Multiplies the elements of two arrays.
    """
    sm = 0
    for i in range(0, len(val_arr)):
        sm = sm + val_arr[i] * arr[i]
    return sm


def change_helper(arr, val_arr, opt_arr, ind, tot):
    """
    A helper function to calculate the smallest
    set of changes equalling a total.
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


def makeChange(arr, tot):
    """
    Calculates the smallest sets of
    changes that equals a total.
    """
    val_arr = []
    opt_arr = []
    for i in range(len(arr)):
        val_arr.append(0)
        opt_arr.append(max(arr))
    ind = 0
    fail_sm = sum(opt_arr)
    change_helper(arr, val_arr, opt_arr, ind, tot)
    if sum(opt_arr) == fail_sm:
        return -1
    return sum(opt_arr)
