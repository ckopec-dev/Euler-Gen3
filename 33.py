from math import gcd

# Euler Problem 33:
# Find the four non-trivial fractions less than one in value where
# the numerator and denominator contain two digits, and cancelling
# one digit from both gives the same fraction.
# The product of all four fractions in lowest terms: find denominator.

numerator_product = 1
denominator_product = 1

for numer in range(10, 100):
    for denom in range(numer + 1, 100):
        n_tens, n_units = numer // 10, numer % 10
        d_tens, d_units = denom // 10, denom % 10

        # Check "curious" cancellations
        # Cancel n_units with d_tens: numer/denom == n_tens/d_units
        if n_units == d_tens and d_units != 0:
            if numer * d_units == denom * n_tens:
                numerator_product *= numer
                denominator_product *= denom

        # Cancel n_tens with d_units: numer/denom == n_units/d_tens
        if n_tens == d_units and d_tens != 0:
            if numer * d_tens == denom * n_units:
                numerator_product *= numer
                denominator_product *= denom

g = gcd(numerator_product, denominator_product)
print(f"Numerator product: {numerator_product}")
print(f"Denominator product: {denominator_product}")
print(f"Answer (denominator in lowest terms): {denominator_product // g}")
