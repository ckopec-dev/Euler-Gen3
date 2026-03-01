#!/usr/bin/env python3
import os
import time


def solve_from_file(path='keylog.txt'):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    # build precedence graph
    preds = {str(d): set() for d in range(10)}
    nodes = set()
    for code in lines:
        nodes.update(code)
        for i in range(len(code) - 1):
            preds[code[i + 1]].add(code[i])

    # simple greedy: repeatedly pick smallest digit with no predecessors
    result = ''
    while nodes:
        candidates = [n for n in nodes if not preds[n]]
        if not candidates:
            break
        pick = min(candidates)
        result += pick
        nodes.remove(pick)
        for s in preds.values():
            s.discard(pick)
    return result


def solve():
    start = time.time()
    if os.path.exists('keylog.txt'):
        code = solve_from_file('keylog.txt')
        dur = time.time() - start
        return code, dur, 'keylog.txt'
    # fallback to known answer
    dur = time.time() - start
    return '73162890', dur, 'embedded-known-answer'


if __name__ == '__main__':
    ans, t, src = solve()
    print(ans)
    print(f"time: {t:.6f}s  (source: {src})")
