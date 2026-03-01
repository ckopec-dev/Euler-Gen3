#!/usr/bin/env python3
import time
import math


def count_combinations_over(limit=1_000_000, max_n=100):
    count = 0
    for n in range(1, max_n + 1):
        for r in range(1, n + 1):
            if math.comb(n, r) > limit:
                count += 1
    return count


def solve():
    start = time.time()
    ans = count_combinations_over()
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
