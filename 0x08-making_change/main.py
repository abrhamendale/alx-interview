#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([125, 25, 2, 1, 5], 292))

print(makeChange([1256, 54, 48, 16, 102], 1453))

#print(makeChange([1256, 54, 48, 16, 102], -1476))

#print(makeChange([100, 100, 100, 100, 100, 100, 100], 30079))
