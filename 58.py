#!/usr/bin/env python3
import time


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n % p == 0:
            return n == p
    # Miller-Rabin deterministic bases for 64-bit
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    def check(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            return True
        if not check(a):
            return False
    return True


def find_side_length(threshold=0.10):
    total_diags = 1
    prime_count = 0
    s = 1
    layer = 0
    while True:
        layer += 1
        s = 2 * layer + 1
        corners = [s * s - i * (s - 1) for i in range(4)]
        for c in corners:
            if is_prime(c):
                prime_count += 1
        total_diags += 4
        ratio = prime_count / total_diags
        if ratio < threshold and layer > 0:
            return s


def solve():
    start = time.time()
    ans = find_side_length(0.10)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
