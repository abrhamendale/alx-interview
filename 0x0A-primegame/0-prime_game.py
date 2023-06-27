#!/usr/bin/python3
"""
Prime game
"""


maria_primes = []
ben_primes = []


def check_multiple(mn, mp, bp):
    """
    Checks if digit is a multiple of.
    """
    for i in mp:
        if mn % i == 0:
            return 0
    for j in bp:
        if mn % j == 0:
            return 0
    return 1


def helper(player, mn, mx):
    """
    A helper function.
    print(player, maria_primes, ben_primes, mn, mx)
    """
    if mn > mx:
        if player == 'Maria':
            return 'Ben'
        else:
            return 'Maria'
    if player == 'Maria':
        if check_multiple(mn, maria_primes, ben_primes):
            maria_primes.append(mn)
        else:
            return helper('Maria', mn + 1, mx)
        return helper('Ben', mn + 1, mx)
    else:
        if check_multiple(mn, maria_primes, ben_primes):
            ben_primes.append(mn)
        else:
            return helper('Ben', mn + 1, mx)
        return helper('Maria', mn + 1, mx)


def isWinner(x, nums):
    """
    Calculates the most winner of the prime game.
    """
    if x == 0 or nums is None:
        return None
    m_count = 0
    b_count = 0
    winner = ''
    for i in range(x):
        if i >= len(nums):
            continue
        if nums[i] != 1:
            winner = helper('Maria', 2, nums[i])
        else:
            winner = 'Ben'
        if winner == 'Maria':
            m_count = m_count + 1
        if winner == 'Ben':
            b_count = b_count + 1
        maria_primes.clear()
        ben_primes.clear()
        winner = ''
    if m_count > b_count:
        return 'Maria'
    if b_count > m_count:
        return 'Ben'
    if m_count == b_count:
        return None
