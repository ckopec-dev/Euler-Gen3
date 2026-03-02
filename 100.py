# Project Euler Problem 100: Arranged probability
#
# If a box contains blue and red discs in the ratio of 1:2, and two discs are drawn at random,
# the probability of both being blue is 1/2. Find the first arrangement of blue and red discs
# where the total number of discs exceeds 10^12.

# The problem can be solved using the recurrence relation derived from the quadratic Diophantine equation:
# b(n+1) = 3*b(n) + 2*t(n) - 2
# t(n+1) = 4*b(n) + 3*t(n) - 3

# Initial values for blue discs (b) and total discs (t)
b, t = 15, 21

# Target: total discs > 10^12
target = 10**12

while t <= target:
    b, t = 3 * b + 2 * t - 2, 4 * b + 3 * t - 3

print(f"Number of blue discs: {b}")
print(f"Total number of discs: {t}")