#!/usr/bin/env python3
import itertools
import time


def polygonal(s, n):
    if s == 3:
        return n * (n + 1) // 2
    if s == 4:
        return n * n
    if s == 5:
        return n * (3 * n - 1) // 2
    if s == 6:
        return n * (2 * n - 1)
    if s == 7:
        return n * (5 * n - 3) // 2
    if s == 8:
        return n * (3 * n - 2)


def gen_4digit(s):
    res = []
    n = 1
    while True:
        p = polygonal(s, n)
        if p >= 10000:
            break
        if p >= 1000:
            res.append(p)
        n += 1
    return res


def find_cycle():
    groups = {s: gen_4digit(s) for s in range(3, 9)}
    # map by first two digits
    by_prefix = {s: {} for s in groups}
    for s, nums in groups.items():
        for num in nums:
            prefix = num // 100
            by_prefix[s].setdefault(prefix, []).append(num)

    # DFS pick one number from each s ensuring chain
    def dfs(path, types):
        if not types:
            # check cyclical
            if str(path[-1])[-2:] == str(path[0])[:2]:
                return path
            return None
        last = path[-1]
        suffix = int(str(last)[-2:])
        for s in types:
            for candidate in by_prefix[s].get(suffix, []):
                res = dfs(path + [candidate], [t for t in types if t != s])
                if res:
                    return res
        return None

    # try all starts
    types = list(range(3, 9))
    for s in types:
        for num in groups[s]:
            remaining = [t for t in types if t != s]
            res = dfs([num], remaining)
            if res:
                return sum(res), res
    return None, None


def solve():
    start = time.time()
    ans, seq = find_cycle()
    dur = time.time() - start
    return ans, dur, seq


if __name__ == '__main__':
    ans, dur, seq = solve()
    print(ans)
    print('sequence:', seq)
    print(f"time: {dur:.6f}s")
