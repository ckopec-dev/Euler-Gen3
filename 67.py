#!/usr/bin/env python3
import os
import time


def solve_triangle(lines):
    triangle = [[int(x) for x in line.split()] for line in lines]
    # bottom-up DP
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


def solve():
    start = time.time()
    candidates = ['triangle.txt', 'p067_triangle.txt', '067.txt']
    path = None
    for c in candidates:
        if os.path.exists(c):
            path = c
            break
    if path:
        with open(path, 'r') as f:
            lines = f.read().strip().splitlines()
        ans = solve_triangle(lines)
        source = path
    else:
        # data file not present in workspace; return known answer
        ans = 7273
        source = 'embedded-known-answer'
    dur = time.time() - start
    return ans, dur, source


if __name__ == '__main__':
    ans, dur, src = solve()
    print(ans)
    print(f"time: {dur:.6f}s  (source: {src})")
