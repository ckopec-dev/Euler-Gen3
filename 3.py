def largest_prime_factor(n):
    last = 1

    while n % 2 == 0:
        last = 2
        n //= 2
    while n % 3 == 0:
        last = 3
        n //= 3

    f = 5
    while f * f <= n:
        while n % f == 0:
            last = f
            n //= f
        while n % (f + 2) == 0:
            last = f + 2
            n //= (f + 2)
        f += 6

    return n if n > 1 else last

print(largest_prime_factor(600851475143))
