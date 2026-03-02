#!/usr/bin/env python3
import time


def count_rectangles(m, n):
    """Count rectangles in m x n grid."""
    return m * (m + 1) * n * (n + 1) // 4


def solve(target=2_000_000):
    start = time.time()
    best_diff = float('inf')
    best_area = 0
    best_m = 0
    best_n = 0
    # search limit: for very large grids, count grows quickly
    # upper bound around 2*sqrt(target) should suffice
    limit = int((2 * target) ** 0.5) + 100
    for m in range(1, limit):
        for n in range(1, limit):
            cnt = count_rectangles(m, n)
            diff = abs(cnt - target)
            if diff < best_diff:
                best_diff = diff
                best_area = m * n
                best_m = m
                best_n = n
            # if count far exceeds target and n is small, can break inner loop
            if cnt > target * 2:
                break
    dur = time.time() - start
    return best_area, best_m, best_n, best_diff, dur


if __name__ == '__main__':
    area, m, n, diff, t = solve()
    print(area)
    print(f"grid: {m} x {n}, rectangles: {count_rectangles(m, n)}, diff: {diff}")
    print(f"time: {t:.6f}s")
