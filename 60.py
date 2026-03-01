#!/usr/bin/env python3
import time
import math


def sieve(limit):
    bs = bytearray(b"\x01") * (limit + 1)
    bs[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if bs[p]:
            step = p
            start = p * p
            bs[start:limit+1:step] = b"\x00" * (((limit - start) // step) + 1)
    return [i for i, v in enumerate(bs) if v]


def is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    def check(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    # Deterministic bases for 64-bit integers
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            return True
        if not check(a):
            return False
    return True


def concat_prime(a: int, b: int, cache: dict) -> bool:
    key = (a, b)
    if key in cache:
        return cache[key]
    val = int(str(a) + str(b))
    res = is_probable_prime(val)
    cache[key] = res
    return res


def find_set(size: int = 5, prime_limit: int = 10000):
    primes = sieve(prime_limit)
    cache = {}

    # Build adjacency lists where concatenations in both orders are prime
    adj = {p: set() for p in primes}
    for i, p in enumerate(primes):
        for q in primes[:i]:
            if concat_prime(p, q, cache) and concat_prime(q, p, cache):
                adj[p].add(q)
                adj[q].add(p)

    best_sum = None

    def search(path: list):
        nonlocal best_sum
        if best_sum is not None and sum(path) >= best_sum:
            return
        if len(path) == size:
            s = sum(path)
            best_sum = s
            print('found set', path, 'sum', s)
            return
        # candidate intersection of neighbors
        candidates = None
        for p in path:
            if candidates is None:
                candidates = set(x for x in adj[p] if x > path[-1])
            else:
                candidates &= adj[p]
        if not candidates:
            return
        for cand in sorted(candidates):
            if best_sum is not None and sum(path) + cand * (size - len(path)) >= best_sum:
                break
            ok = True
            for prev in path:
                if cand not in adj[prev]:
                    ok = False
                    break
            if ok:
                search(path + [cand])

    for p in primes:
        if best_sum is not None and p * size >= best_sum:
            break
        if adj[p]:
            search([p])
            if best_sum is not None:
                return best_sum
    return best_sum


def solve():
    start = time.time()
    ans = find_set(5, 10000)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
