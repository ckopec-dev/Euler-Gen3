#!/usr/bin/env python3
import math
import time


def solve(limit=1_000_000):
    start = time.time()
    best_n = 0
    best_d = 1
    for d in range(1, limit + 1):
        # largest n with n/d < 3/7
        n = (3 * d - 1) // 7
        if math.gcd(n, d) == 1:
            if n * best_d > best_n * d:
                best_n, best_d = n, d
    dur = time.time() - start
    return best_n, best_d, dur


if __name__ == '__main__':
    n, d, t = solve()
    print(f"{n}/{d}")
    print(n)
    print(f"time: {t:.6f}s")
