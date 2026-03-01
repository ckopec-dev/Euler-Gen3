#!/usr/bin/env python3
import time


def sieve(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:limit+1:step] = b"\x00" * (((limit - start) // step) + 1)
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes, set(primes)


def find_prime_family(family_size=8, limit=1000000):
    primes, prime_set = sieve(limit)
    for p in primes:
        s = str(p)
        L = len(s)
        for mask in range(1, 1 << L):
            digits = {s[pos] for pos in range(L) if (mask >> pos) & 1}
            if len(digits) != 1:
                continue
            target_count = 0
            contains_original = False
            for replacement in '0123456789':
                lst = list(s)
                for pos in range(L):
                    if (mask >> pos) & 1:
                        lst[pos] = replacement
                if lst[0] == '0':
                    continue
                val = int(''.join(lst))
                if val in prime_set:
                    target_count += 1
                    if val == p:
                        contains_original = True
            if target_count == family_size and contains_original:
                return p
    return None


def solve():
    start = time.time()
    ans = find_prime_family(8, 1000000)
    dur = time.time() - start
    return ans, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.3f}s")
