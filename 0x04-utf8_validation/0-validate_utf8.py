#!/usr/bin/python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """Checks if data is a valid utf-8 encoding"""
    if data is None:
        return (False)
    try:
        int(data[0])
    except ValueError:
        return (False)
    data = iter(data)
    for msbs in data:
        msb_ones = 8
        for i in range(8):
            if msbs >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
                msb_ones = i
        if msb_ones in [1, 7, 8]:
            return False
        for _ in range(msb_ones - 1):
            lsbs = next(data, None)
            if lsbs is None or lsbs >> 6 != 0b10:
                return False
    return True
