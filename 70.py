#!/usr/bin/env python3
import time
import math


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n+1:step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i, v in enumerate(sieve) if v]


def is_perm(a, b):
    return ''.join(sorted(str(a))) == ''.join(sorted(str(b)))


def solve(limit=10_000_000):
    start = time.time()
    # search products of two primes p<q
    primes = primes_upto(100000)
    best_n = None
    best_ratio = float('inf')
    for i, p in enumerate(primes):
        if p * p > limit:
            break
        for q in primes[i + 1:]:
            n = p * q
            if n > limit:
                break
            phi = (p - 1) * (q - 1)
            if is_perm(n, phi):
                ratio = n / phi
                if ratio < best_ratio:
                    best_ratio = ratio
                    best_n = n
    dur = time.time() - start
    return best_n, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
