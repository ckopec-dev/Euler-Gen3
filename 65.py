#!/usr/bin/env python3
import time


def e_continued_fraction_terms(n_terms=100):
    terms = [2]
    k = 1
    while len(terms) < n_terms:
        terms.extend([1, 2 * k, 1])
        k += 1
    return terms[:n_terms]


def convergent_num_den(terms):
    from fractions import Fraction
    frac = Fraction(0, 1)
    for a in reversed(terms[1:]):
        frac = 1 / (a + frac)
    frac = terms[0] + frac
    return frac.numerator, frac.denominator


def solve():
    start = time.time()
    terms = e_continued_fraction_terms(100)
    num, den = convergent_num_den(terms)
    s = sum(int(d) for d in str(num))
    dur = time.time() - start
    return s, dur


if __name__ == '__main__':
    ans, dur = solve()
    print(ans)
    print(f"time: {dur:.6f}s")
