import math

def is_pentagonal(n):
    k = (1 + math.sqrt(1 + 24 * n)) / 6
    return abs(k - round(k)) < 1e-9

# Hexagonal numbers are always triangular, so we only need to check
# if a hexagonal number is also pentagonal.
# H(143) = P(165) = T(285) = 40755 is the known starting point.
# Start searching from H(144) onwards.

n = 144
while True:
    h = n * (2 * n - 1)  # Hexagonal formula
    if is_pentagonal(h):
        print(f"H({n}) = {h}")
        break
    n += 1