"""
Euler Problem 23: Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
An abundant number is a number for which the sum of its proper divisors exceeds the number.

It can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
Find the sum of all positive integers which cannot be written as the sum of two abundant numbers.
"""

def sum_of_divisors(n):
    if n == 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

LIMIT = 28123

# Find all abundant numbers up to LIMIT
abundants = [n for n in range(1, LIMIT + 1) if sum_of_divisors(n) > n]

# Build a set of all numbers that ARE the sum of two abundant numbers
abundant_set = set(abundants)
sums = set()
for i, a in enumerate(abundants):
    for b in abundants[i:]:
        s = a + b
        if s > LIMIT:
            break
        sums.add(s)

# Sum all positive integers that cannot be written as the sum of two abundant numbers
result = sum(n for n in range(1, LIMIT + 1) if n not in sums)
print(f"Answer: {result}")