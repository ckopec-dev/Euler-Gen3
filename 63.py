#!/usr/bin/env python3
import time


def count_n_digit_nth_powers(limit_base=9):
    count = 0
    for a in range(1, limit_base + 1):
        n = 1
        while True:
            v = a ** n
            if len(str(v)) < n:
                break
            if len(str(v)) == n:
                count += 1
            n += 1
    return count


def solve():
    start = time.time()
    ans = count_n_digit_nth_powers()
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
