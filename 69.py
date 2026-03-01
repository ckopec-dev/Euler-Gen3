#!/usr/bin/env python3
import time


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n+1:step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i, v in enumerate(sieve) if v]


def solve(limit=1_000_000):
    start = time.time()
    prod = 1
    for p in primes_upto(100):
        if prod * p > limit:
            break
        prod *= p
    dur = time.time() - start
    return prod, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
