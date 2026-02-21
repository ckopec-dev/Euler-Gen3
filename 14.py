"""
Euler Problem 14:
The following iterative sequence is defined for the set of positive integers:
  n → n/2 (n is even)
  n → 3n + 1 (n is odd)

Which starting number, under one million, produces the longest Collatz chain?
"""

import sys
sys.setrecursionlimit(10000)

def solve():
    cache = {1: 1}

    def collatz_length(n):
        if n in cache:
            return cache[n]
        if n % 2 == 0:
            length = 1 + collatz_length(n // 2)
        else:
            length = 1 + collatz_length(3 * n + 1)
        cache[n] = length
        return length

    max_len = 0
    result = 0
    for i in range(1, 1_000_000):
        length = collatz_length(i)
        if length > max_len:
            max_len = length
            result = i

    print(f"Starting number: {result}")
    print(f"Chain length:    {max_len}")

solve()