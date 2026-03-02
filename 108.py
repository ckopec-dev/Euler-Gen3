"""
Problem 108: Diophantine reciprocals I

In the equation 1/x + 1/y = 1/n, for x, y, n positive integers.
When n = 4k + 2, there cannot be more than one solution.

We need to find the lowest value of n for which the number of distinct solutions
exceeds 1000.

From 1/x + 1/y = 1/n, we can derive:
x = n(n+d) / d where d divides n^2

So the number of solutions is related to the number of divisors of n^2.
Specifically, the number of positive solutions is (τ(n^2) + 1) / 2
where τ is the divisor count function.
"""

def count_divisors(n):
    """Count number of divisors of n"""
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i * i != n:
                count += 1
        i += 1
    return count

def count_solutions(n):
    """Count number of distinct solutions to 1/x + 1/y = 1/n"""
    n_squared = n * n
    divisors = count_divisors(n_squared)
    # Number of solutions is (divisors + 1) // 2
    return (divisors + 1) // 2

def prime_factorization(n):
    """Get prime factorization as dict {prime: exponent}"""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def count_divisors_from_factors(factors):
    """Count divisors from prime factorization"""
    count = 1
    for exp in factors.values():
        count *= (exp + 1)
    return count

def count_solutions_optimized(n):
    """Count solutions using prime factorization"""
    factors = prime_factorization(n)
    # For n^2, all exponents are doubled
    divisor_count = 1
    for exp in factors.values():
        divisor_count *= (2 * exp + 1)
    return (divisor_count + 1) // 2

def solve():
    n = 1
    while True:
        solutions = count_solutions_optimized(n)
        if solutions > 1000:
            return n
        n += 1
        if n > 1000000:  # safety check
            break
    return -1

if __name__ == '__main__':
    result = solve()
    print(f"Answer: {result}")
