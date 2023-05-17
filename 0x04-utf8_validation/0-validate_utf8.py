#!/usr/bin/python3
"""
UTF-8 validation module
"""

def validUTF8(data):
    """Checks if an input is a valid UTF-8 encoding."""
    for i in range(0, len(data)):
        if int(data[i]) > 255:
            return (False)
    return (True)
