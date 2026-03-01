def count_prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return len(factors)

def solve(consecutive=4, distinct=4):
    count = 0
    n = 2
    while True:
        if count_prime_factors(n) == distinct:
            count += 1
            if count == consecutive:
                return n - consecutive + 1
        else:
            count = 0
        n += 1

print(solve())  # 134043