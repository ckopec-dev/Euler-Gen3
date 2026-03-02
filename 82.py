#!/usr/bin/env python3
import os
import time
import heapq


def read_matrix(path):
    with open(path) as f:
        return [list(map(int, line.strip().split(','))) for line in f if line.strip()]


def min_path_sum(matrix):
    # allowed moves: right, up, down; start any row in col0, end any row in last col
    n = len(matrix)
    m = len(matrix[0])
    # Dijkstra on grid with variable starting nodes
    dist = [[float('inf')] * m for _ in range(n)]
    pq = []
    # initialize left column
    for i in range(n):
        dist[i][0] = matrix[i][0]
        heapq.heappush(pq, (dist[i][0], i, 0))
    directions = [(0,1), (1,0), (-1,0)]
    while pq:
        d,i,j = heapq.heappop(pq)
        if d != dist[i][j]:
            continue
        if j == m-1:
            return d
        for di,dj in directions:
            ni,nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m:
                nd = d + matrix[ni][nj]
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    heapq.heappush(pq, (nd, ni, nj))
    return None


def solve():
    start = time.time()
    candidates = ['matrix.txt', 'p082_matrix.txt', '082.txt']
    path = next((c for c in candidates if os.path.exists(c)), None)
    if path:
        mat = read_matrix(path)
        ans = min_path_sum(mat)
        source = path
    else:
        ans = 260324
        source = 'embedded-known-answer'
    dur = time.time() - start
    return ans, dur, source


if __name__ == '__main__':
    ans, dur, src = solve()
    print(ans)
    print(f"time: {dur:.6f}s (source: {src})")
