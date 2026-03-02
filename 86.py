"""
Project Euler - Problem 86

A spider sits in one corner of a cuboid room, and a fly sits in the opposite corner.
By considering cuboids with integer dimensions up to M x M x M, find the least value
of M such that the number of cuboid solutions first exceeds one million.

Key insight:
  For a cuboid with dimensions a x b x c (where c is the largest),
  the shortest surface path is found by unfolding the room into a flat rectangle.
  The shortest unfolding gives distance: sqrt((a+b)^2 + c^2)
  For this to be an integer, (a+b)^2 + c^2 must be a perfect square.

Algorithm:
  - Let s = a + b. For each new c = M, check all values of s from 2 to 2c.
  - If s^2 + c^2 is a perfect square, count valid integer pairs (a, b)
    where a <= b <= c and a + b = s.
  - Valid a values: max(1, s-c) <= a <= s//2
  - Accumulate count until it exceeds 1,000,000.
"""

import math


def solve(target=1_000_000):
    count = 0
    M = 0

    while count <= target:
        M += 1
        c = M

        # s = a + b, ranges from 2 (min: a=b=1) to 2c (max: a=b=c)
        for s in range(2, 2 * c + 1):
            val = s * s + c * c
            sq = int(math.isqrt(val))

            if sq * sq == val:  # perfect square — integer path length!
                # Count pairs (a, b) with a <= b <= c and a + b = s
                # a <= b        =>  a <= s // 2
                # b <= c        =>  s - a <= c  =>  a >= s - c
                lo = max(1, s - c)
                hi = s // 2
                if hi >= lo:
                    count += hi - lo + 1

    return M


result = solve()
print(f"Answer: {result}")