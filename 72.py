#!/usr/bin/env python3
import time


def totient_sieve(n):
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi


def solve(limit=1_000_000):
    start = time.time()
    phi = totient_sieve(limit)
    ans = sum(phi[2:])
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, t = solve()
    print(ans)
    print(f"time: {t:.6f}s")
