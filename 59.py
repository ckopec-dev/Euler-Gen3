#!/usr/bin/env python3
import os
import time


def load_cipher(path='cipher1.txt'):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        data = f.read().strip()
    nums = [int(x) for x in data.split(',') if x]
    return nums


def decrypt(nums, key):
    out = []
    klen = len(key)
    for i, n in enumerate(nums):
        out.append(n ^ key[i % klen])
    return bytes(out)


def find_key_and_sum(nums):
    best = None
    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                key = (a, b, c)
                plain = decrypt(nums, key)
                try:
                    text = plain.decode('ascii')
                except UnicodeDecodeError:
                    continue
                if ' the ' in text or ' and ' in text:
                    return key, text, sum(plain)
    return None, None, None


def solve():
    start = time.time()
    nums = load_cipher('cipher1.txt')
    if nums is None:
        return None, None, None, 0.0
    key, text, s = find_key_and_sum(nums)
    dur = time.time() - start
    return key, text, s, dur


if __name__ == '__main__':
    key, text, s, dur = solve()
    if key is None:
        print('cipher1.txt not found or key not determined')
    else:
        print('key:', ''.join(map(chr, key)))
        print('sum:', s)
        print('time: {:.6f}s'.format(dur))
