def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def same_digits(a, b, c):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

primes = [n for n in range(1000, 10000) if is_prime(n)]
prime_set = set(primes)

for i, p1 in enumerate(primes):
    for p2 in primes[i+1:]:
        diff = p2 - p1
        p3 = p2 + diff
        if p3 in prime_set and same_digits(p1, p2, p3):
            print(f"{p1}, {p2}, {p3} → {p1}{p2}{p3}")