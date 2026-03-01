#!/usr/bin/env python3
import time


def find_smallest_cube_with_perms(target_count=5):
    cubes = {}
    n = 1
    while True:
        c = n ** 3
        key = ''.join(sorted(str(c)))
        cubes.setdefault(key, []).append(c)
        if len(cubes[key]) == target_count:
            return min(cubes[key])
        n += 1


def solve():
    start = time.time()
    ans = find_smallest_cube_with_perms(5)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
