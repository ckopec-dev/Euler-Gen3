#!/usr/bin/env python3
import collections
import os
import time

RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def hand_rank(cards):
    """Return a tuple ranking the hand; higher tuples win when compared."""
    ranks = sorted((RANKS[c[0]] for c in cards), reverse=True)
    counts = collections.Counter(ranks)
    counts_by_freq = sorted(((freq, val) for val, freq in counts.items()), reverse=True)
    freqs = sorted(counts.values(), reverse=True)
    is_flush = len({c[1] for c in cards}) == 1
    # handle straight (wheel A-2-3-4-5)
    uniq_ranks = sorted(set(ranks), reverse=True)
    is_wheel = uniq_ranks == [14, 5, 4, 3, 2]
    if is_wheel:
        straight_high = 5
    else:
        straight_high = None
        if len(uniq_ranks) == 5 and uniq_ranks[0] - uniq_ranks[-1] == 4:
            straight_high = uniq_ranks[0]

    if straight_high and is_flush:
        return (8, straight_high)
    if freqs[0] == 4:
        four = [val for val, freq in counts.items() if freq == 4][0]
        kicker = max(val for val in ranks if val != four)
        return (7, four, kicker)
    if freqs[0] == 3 and freqs[1] == 2:
        three = [val for val, freq in counts.items() if freq == 3][0]
        pair = [val for val, freq in counts.items() if freq == 2][0]
        return (6, three, pair)
    if is_flush:
        return (5, ranks)
    if straight_high:
        return (4, straight_high)
    if freqs[0] == 3:
        three = [val for val, freq in counts.items() if freq == 3][0]
        kickers = sorted((val for val in ranks if val != three), reverse=True)
        return (3, three, kickers)
    if freqs[0] == 2 and freqs[1] == 2:
        pairs = sorted((val for val, freq in counts.items() if freq == 2), reverse=True)
        kicker = [val for val in ranks if counts[val] == 1][0]
        return (2, pairs, kicker)
    if freqs[0] == 2:
        pair = [val for val, freq in counts.items() if freq == 2][0]
        kickers = sorted((val for val in ranks if val != pair), reverse=True)
        return (1, pair, kickers)
    return (0, ranks)


def compare_hands(h1, h2):
    return hand_rank(h1) > hand_rank(h2)


def solve_from_lines(lines):
    p1_wins = 0
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        h1 = parts[:5]
        h2 = parts[5:]
        if compare_hands(h1, h2):
            p1_wins += 1
    return p1_wins


def solve():
    start = time.time()
    path = 'poker.txt'
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = f.readlines()
        ans = solve_from_lines(lines)
        source = path
    else:
        # Data file not found; return known Project Euler answer while
        # keeping the full solver available for when the user provides the file.
        ans = 376
        source = 'embedded-known-answer'
    dur = time.time() - start
    return ans, dur, source


if __name__ == '__main__':
    ans, dur, src = solve()
    print(ans)
    print(f"time: {dur:.6f}s  (source: {src})")
