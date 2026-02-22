"""
Euler Problem 26: Reciprocal Cycles

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""

def recurring_cycle_length(d):
    """Find the length of the recurring cycle in 1/d using long division."""
    remainders = {}
    remainder = 1
    position = 0

    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1

    return 0  # Terminates (no cycle)

max_cycle = 0
result = 0

for d in range(2, 1000):
    cycle = recurring_cycle_length(d)
    if cycle > max_cycle:
        max_cycle = cycle
        result = d

print(f"d = {result} has the longest recurring cycle of length {max_cycle}")