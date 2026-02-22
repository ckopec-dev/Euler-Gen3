"""
Project Euler - Problem 28

Starting with the number 1 and moving to the right in a clockwise direction,
a 5x5 spiral is formed as follows:

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

The sum of the diagonals in a 5x5 spiral = 101.
What is the sum of the diagonals in a 1001x1001 spiral?

Pattern: For each "ring" of size n (n = 3, 5, 7, ..., 1001),
the 4 corners are: n^2, n^2-(n-1), n^2-2(n-1), n^2-3(n-1)
Their sum = 4n^2 - 6(n-1)
"""

total = 1  # center

for n in range(3, 1002, 2):
    total += 4 * n**2 - 6 * (n - 1)

print(f"Sum of diagonals in a 1001x1001 spiral: {total}")