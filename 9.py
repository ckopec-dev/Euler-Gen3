# Euler Problem 9
# Find the Pythagorean triplet where a + b + c = 1000, then compute a * b * c.
# A Pythagorean triplet satisfies: a^2 + b^2 = c^2, with a < b < c

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if c > b and a*a + b*b == c*c:
            print(f"a={a}, b={b}, c={c}")
            print(f"a + b + c = {a + b + c}")
            print(f"a * b * c = {a * b * c}")
            break