#!/usr/bin/env python3
import math
import time


def solve(limit=1_500_000):
    start = time.time()
    counts = [0] * (limit + 1)
    m = 2
    while 2 * m * (m + 1) <= limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                p0 = a + b + c
                k = p0
                while k <= limit:
                    counts[k] += 1
                    k += p0
        m += 1
    ans = sum(1 for x in counts if x == 1)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, t = solve()
    print(ans)
    print(f"time: {t:.6f}s")
