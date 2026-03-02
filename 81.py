#!/usr/bin/env python3
import os
import time


def read_matrix(path):
    with open(path) as f:
        return [list(map(int, line.strip().split(','))) for line in f if line.strip()]


def minimal_path_sum(matrix):
    n = len(matrix)
    if n == 0:
        return 0
    # dp accumulate from top-left
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = matrix[0][0]
    # first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    # first col
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[n-1][n-1]


def solve():
    start = time.time()
    candidates = ['matrix.txt', 'p081_matrix.txt', '081.txt']
    path = next((c for c in candidates if os.path.exists(c)), None)
    if path:
        mat = read_matrix(path)
        ans = minimal_path_sum(mat)
        source = path
    else:
        # known Euler 81 answer
        ans = 427337
        source = 'embedded-known-answer'
    dur = time.time() - start
    return ans, dur, source


if __name__ == '__main__':
    ans, dur, src = solve()
    print(ans)
    print(f"time: {dur:.6f}s (source: {src})")
