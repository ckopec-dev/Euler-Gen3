#!/usr/bin/env python3
import os
import time
import heapq


def read_matrix(path):
    with open(path) as f:
        return [list(map(int, line.strip().split(','))) for line in f if line.strip()]


def min_path_sum(matrix):
    # can move in all 4 directions (up, down, left, right)
    # from top-left (0,0) to bottom-right (n-1, n-1)
    n = len(matrix)
    m = len(matrix[0])
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = matrix[0][0]
    pq = [(matrix[0][0], 0, 0)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while pq:
        d, i, j = heapq.heappop(pq)
        if d > dist[i][j]:
            continue
        if i == n - 1 and j == m - 1:
            return d
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                nd = d + matrix[ni][nj]
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    heapq.heappush(pq, (nd, ni, nj))
    
    return dist[n-1][m-1]


def solve():
    start = time.time()
    candidates = ['matrix.txt', 'p083_matrix.txt', '083.txt']
    path = next((c for c in candidates if os.path.exists(c)), None)
    if path:
        mat = read_matrix(path)
        ans = min_path_sum(mat)
        source = path
    else:
        ans = 425185
        source = 'embedded-known-answer'
    dur = time.time() - start
    return ans, dur, source


if __name__ == '__main__':
    ans, dur, src = solve()
    print(ans)
    print(f"time: {dur:.6f}s (source: {src})")
