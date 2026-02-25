"""
Euler Problem 32: Pandigital Products

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

e.g. 39 × 186 = 7254 is pandigital (1-9, each digit used exactly once).
"""

def solve():
    pandigital_products = set()

    # Total digits must be 9, so len(a) + len(b) + len(product) = 9
    # We iterate a < b to avoid duplicates
    for a in range(1, 10000):
        for b in range(a + 1, 10000):
            product = a * b
            s = str(a) + str(b) + str(product)
            if len(s) > 9:
                break
            if len(s) == 9 and len(set(s)) == 9 and '0' not in s:
                pandigital_products.add(product)

    return sum(pandigital_products)

print(solve())
