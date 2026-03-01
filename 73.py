#!/usr/bin/env python3
import math
import time


def solve(limit=12000):
    start = time.time()
    cnt = 0
    for d in range(2, limit + 1):
        low = d // 3 + 1
        high = (d - 1) // 2
        for n in range(low, high + 1):
            if math.gcd(n, d) == 1:
                cnt += 1
    dur = time.time() - start
    return cnt, dur


if __name__ == '__main__':
    ans, t = solve()
    print(ans)
    print(f"time: {t:.6f}s")
