#!/usr/bin/env python3
import math
import time


def digital_sum_sqrt(limit=100):
    total = 0
    for n in range(1, limit + 1):
        a = int(math.isqrt(n))
        if a * a == n:
            continue
        # compute floor(sqrt(n) * 10**100)
        scaled = math.isqrt(n * 10 ** 200)
        s = str(scaled).rjust(101, '0')[:100]
        total += sum(int(ch) for ch in s)
    return total


def solve():
    start = time.time()
    ans = digital_sum_sqrt(100)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, t = solve()
    print(ans)
    print(f"time: {t:.6f}s")
