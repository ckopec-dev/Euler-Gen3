#!/usr/bin/env python3
import itertools
import time


def max_magic_5gon():
    nums = list(range(1, 11))
    best = 0
    best_seq = None
    # choose 5 outer nodes as combination; enforce smallest outer node as first to canonicalize
    for outer in itertools.permutations(nums, 5):
        outer_set = set(outer)
        inner = [n for n in nums if n not in outer_set]
        # canonicalize so outer[0] is minimal among outer
        if outer[0] != min(outer):
            continue
        # iterate permutations of inner
        for inn_perm in itertools.permutations(inner):
            lines = []
            valid = True
            s = None
            for i in range(5):
                a = outer[i]
                b = inn_perm[i]
                c = inn_perm[(i + 1) % 5]
                line_sum = a + b + c
                if s is None:
                    s = line_sum
                elif line_sum != s:
                    valid = False
                    break
                lines.append(f"{a}{b}{c}")
            if valid:
                concat = ''.join(lines)
                if len(concat) == 16:
                    val = int(concat)
                    if val > best:
                        best = val
                        best_seq = (outer, inn_perm, concat)
    return best, best_seq


def solve():
    start = time.time()
    # brute-force may be expensive but should finish within reasonable time
    ans, seq = max_magic_5gon()
    dur = time.time() - start
    return ans, dur, seq


if __name__ == '__main__':
    ans, dur, seq = solve()
    print(ans)
    print('sequence:', seq)
    print(f"time: {dur:.6f}s")
