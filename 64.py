#!/usr/bin/env python3
import time
import math


def period_sqrt(n):
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return 0
    m = 0
    d = 1
    a = a0
    period = 0
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1
        if a == 2 * a0:
            return period


def count_odd_periods(limit=10000):
    c = 0
    for n in range(2, limit + 1):
        if period_sqrt(n) % 2 == 1:
            c += 1
    return c


def solve():
    start = time.time()
    ans = count_odd_periods(10000)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
