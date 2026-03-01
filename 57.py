#!/usr/bin/env python3
import time


def count_longer_numerators(n_iters=1000):
    p, q = 1, 1
    count = 0
    for _ in range(n_iters):
        p, q = p + 2 * q, p + q
        if len(str(p)) > len(str(q)):
            count += 1
    return count


def solve():
    start = time.time()
    ans = count_longer_numerators(1000)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
