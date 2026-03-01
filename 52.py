#!/usr/bin/env python3
import time


def find_smallest(limit=2000000):
    n = 1
    while n <= limit:
        s = sorted(str(n))
        ok = True
        for k in range(2, 7):
            if sorted(str(n * k)) != s:
                ok = False
                break
        if ok:
            return n
        n += 1
    return None


def solve():
    start = time.time()
    ans = find_smallest()
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.3f}s")
