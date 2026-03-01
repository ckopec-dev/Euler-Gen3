#!/usr/bin/env python3
import time
import math


def cont_frac_sqrt(D):
    a0 = int(math.isqrt(D))
    if a0 * a0 == D:
        return []
    m = 0
    d = 1
    a = a0
    seq = []
    seen = set()
    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        seq.append(a)
        if a == 2 * a0:
            break
    return seq


def minimal_pell_x(D):
    a0 = int(math.isqrt(D))
    if a0 * a0 == D:
        return None
    seq = cont_frac_sqrt(D)
    # build convergents until solution
    p0, q0 = a0, 1
    # start with first term
    p_prev2, q_prev2 = 1, 0
    p_prev1, q_prev1 = a0, 1
    k = 0
    while True:
        a = seq[k % len(seq)]
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        if p * p - D * q * q == 1:
            return p
        p_prev2, q_prev2 = p_prev1, q_prev1
        p_prev1, q_prev1 = p, q
        k += 1


def solve():
    start = time.time()
    best_D = 0
    best_x = 0
    for D in range(2, 1001):
        x = minimal_pell_x(D)
        if x is None:
            continue
        if x > best_x:
            best_x = x
            best_D = D
    dur = time.time() - start
    return best_D, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
