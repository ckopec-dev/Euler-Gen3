# Solution to Project Euler Problem 94
# Problem Statement: https://projecteuler.net/problem=94

# The problem involves finding almost equilateral triangles with integral side lengths
# and area, where the side lengths are in the form (a, a, a+1) or (a, a, a-1).

# Importing math for square root calculation
import math

def is_perfect_square(n):
    """Check if a number is a perfect square."""
    if n < 0:
        return False
    root = int(math.isqrt(n))
    return root * root == n

def solve_problem_94(limit):
    """Solve the problem for a given perimeter limit."""
    total_perimeter = 0

    # Check for triangles of the form (a, a, a+1)
    a = 2
    while 3 * a + 1 <= limit:
        area_squared = a * a * (a + 1) * (a - 1)
        if is_perfect_square(area_squared):
            total_perimeter += 3 * a + 1
        a += 1

    # Check for triangles of the form (a, a, a-1)
    a = 2
    while 3 * a - 1 <= limit:
        area_squared = a * a * (a + 1) * (a - 1)
        if is_perfect_square(area_squared):
            total_perimeter += 3 * a - 1
        a += 1

    return total_perimeter

if __name__ == "__main__":
    # The problem specifies a perimeter limit of 1 billion
    perimeter_limit = 10**9
    result = solve_problem_94(perimeter_limit)
    print("The sum of the perimeters of all almost equilateral triangles is:", result)