"""
Euler Problem 6: Sum Square Difference

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

n = 100

sum_of_squares = sum(i**2 for i in range(1, n + 1))
square_of_sum = sum(range(1, n + 1)) ** 2

result = square_of_sum - sum_of_squares

print(f"Sum of squares:  {sum_of_squares}")
print(f"Square of sum:   {square_of_sum}")
print(f"Difference:      {result}")