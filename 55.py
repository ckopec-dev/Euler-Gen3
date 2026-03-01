#!/usr/bin/env python3
import time


def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def is_lychrel(n: int, max_iters: int = 50) -> bool:
    curr = n
    for _ in range(max_iters):
        rev = int(str(curr)[::-1])
        curr = curr + rev
        if is_palindrome(curr):
            return False
    return True


def count_lychrel(limit: int = 10000) -> int:
    count = 0
    for n in range(1, limit):
        if is_lychrel(n):
            count += 1
    return count


def solve():
    start = time.time()
    ans = count_lychrel(10000)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
