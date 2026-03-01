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


def find(limit=1000, target=5000):
    start = time.time()
    primes = primes_upto(limit)
    ways = [0] * (limit + 1)
    ways[0] = 1
    for p in primes:
        for s in range(p, limit + 1):
            ways[s] += ways[s - p]
    for n in range(2, limit + 1):
        if ways[n] > target and n in primes:
            return n, time.time() - start
    return None, time.time() - start


if __name__ == '__main__':
    # incrementally increase limit until found
    lim = 100
    while True:
        ans, t = find(lim, 5000)
        if ans:
            print(ans)
            print(f"time: {t:.6f}s")
            break
        lim *= 2
