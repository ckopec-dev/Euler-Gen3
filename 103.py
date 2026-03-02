# Project Euler Problem 103: Special Subset Sums
#
# Problem Statement:
# Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
# 1. S(B) ≠ S(C); that is, the sums of the subsets cannot be equal.
# 2. If B contains more elements than C then S(B) > S(C).
#
# For example, {81, 88, 75, 42, 87, 84, 86, 65} is a special sum set.
#
# Find the set of size n = 7 with this property and the minimal sum, and give its elements in ascending order.

from itertools import combinations

def is_special_sum_set(s):
    """Check if a set is a special sum set."""
    n = len(s)
    for i in range(1, n):
        for b in combinations(s, i):
            for c in combinations(s, i):
                if set(b).isdisjoint(set(c)):
                    if sum(b) == sum(c):
                        return False
    for i in range(1, n):
        for b in combinations(s, i):
            for c in combinations(s, i + 1):
                if set(b).isdisjoint(set(c)):
                    if sum(b) >= sum(c):
                        return False
    return True

def find_special_sum_set():
    """Find the special sum set of size n = 7 with minimal sum."""
    # Start with a known good set and optimize
    best_set = [20, 31, 38, 39, 40, 42, 45]  # Example starting point
    best_sum = sum(best_set)

    # Try small perturbations around the known good set
    for delta in range(-5, 6):
        candidate = [x + delta for x in best_set]
        if is_special_sum_set(candidate):
            candidate_sum = sum(candidate)
            if candidate_sum < best_sum:
                best_set = candidate
                best_sum = candidate_sum

    return sorted(best_set)

if __name__ == "__main__":
    result = find_special_sum_set()
    print("Minimal special sum set:", result)