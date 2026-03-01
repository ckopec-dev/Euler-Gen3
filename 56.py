#!/usr/bin/env python3
import time


def digit_sum(n: int) -> int:
    return sum(map(int, str(n)))


def max_digital_sum(limit=100):
    best = 0
    best_pair = (0, 0)
    for a in range(1, limit):
        for b in range(1, limit):
            s = digit_sum(pow(a, b))
            if s > best:
                best = s
                best_pair = (a, b)
    return best, best_pair


def solve():
    start = time.time()
    ans, pair = max_digital_sum(100)
    dur = time.time() - start
    return ans, pair, dur


if __name__ == '__main__':
    ans, pair, dur = solve()
    print(ans)
    print(f"best a,b: {pair}")
    print(f"time: {dur:.6f}s")
