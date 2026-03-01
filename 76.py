#!/usr/bin/env python3
import time


def solve(n=100):
    start = time.time()
    ways = [1] + [0] * n
    for k in range(1, n):
        for s in range(k, n + 1):
            ways[s] += ways[s - k]
    # exclude the partition consisting of n itself
    ans = ways[n] - 1
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, t = solve()
    print(ans)
    print(f"time: {t:.6f}s")
