# Problem 99: Largest exponential
# https://projecteuler.net/problem=99

import math

def read_base_exp_pairs(file_path):
    """Reads the base and exponent pairs from a file."""
    with open(file_path, 'r') as file:
        pairs = [tuple(map(int, line.strip().split(','))) for line in file]
    return pairs

def find_largest_exponential(file_path):
    """Finds the line number with the largest exponential value."""
    pairs = read_base_exp_pairs(file_path)
    max_value = -math.inf
    max_line = -1

    for i, (base, exp) in enumerate(pairs, start=1):
        # Use logarithmic comparison to avoid overflow
        value = exp * math.log(base)
        if value > max_value:
            max_value = value
            max_line = i

    return max_line

if __name__ == "__main__":
    file_path = "base_exp.txt"
    result = find_largest_exponential(file_path)
    print(f"The line number with the largest exponential value is: {result}")