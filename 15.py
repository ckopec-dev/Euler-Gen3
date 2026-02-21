"""
Euler Problem 15: Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to
move right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Solution: This is a combinatorics problem. To traverse a 20x20 grid,
you must make exactly 20 right moves and 20 down moves (40 total).
The answer is C(40, 20) = 40! / (20! * 20!)
"""

from math import comb

result = comb(40, 20)
print(f"Number of lattice paths through a 20x20 grid: {result}")