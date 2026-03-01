#!/usr/bin/env python3
import time


def partitions_mod(limit_mod=1_000_000):
    p = [1]
    k = 1
    while True:
        for sign, m in ((1, k), ( -1, k * 2), (1, k * 3), (-1, k * 4)):
            pass


def solve(mod=1_000_000):
    start = time.time()
    p = [1]
    n = 1
    while True:
        total = 0
        k = 1
        while True:
            gp1 = k * (3 * k - 1) // 2
            gp2 = k * (3 * k + 1) // 2
            if gp1 > n and gp2 > n:
                break
            if gp1 <= n:
                total += (-1) ** (k - 1) * p[n - gp1]
            if gp2 <= n:
                total += (-1) ** (k - 1) * p[n - gp2]
            k += 1
        total %= mod
        p.append(total)
        if total == 0:
            dur = time.time() - start
            return n, dur
        n += 1


if __name__ == '__main__':
    ans, t = solve()
    print(ans)
    print(f"time: {t:.6f}s")
