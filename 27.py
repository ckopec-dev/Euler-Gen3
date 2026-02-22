"""
Euler Problem 27:
Find the product a*b where |a| < 1000 and |b| < 1000, for the quadratic formula
n^2 + an + b that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_consecutive_primes(a, b):
    n = 0
    while is_prime(n*n + a*n + b):
        n += 1
    return n

best_count = 0
best_product = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        count = count_consecutive_primes(a, b)
        if count > best_count:
            best_count = count
            best_product = a * b
            best_a, best_b = a, b

print(f"Best a = {best_a}, b = {best_b}")
print(f"Consecutive primes: {best_count}")
print(f"Answer (a * b) = {best_product}")