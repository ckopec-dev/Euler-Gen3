from math import isqrt

def word_value(word):
    return sum(ord(c) - ord('A') + 1 for c in word)

def is_triangle(n):
    # A number t is triangular if sqrt(8t+1) is a perfect integer
    discriminant = 8 * n + 1
    root = isqrt(discriminant)
    return root * root == discriminant

with open("42.txt") as f: content = f.read()

words = [w.strip('"') for w in content.split(',')]

count = sum(1 for word in words if is_triangle(word_value(word)))
print(f"Number of triangle words: {count}")