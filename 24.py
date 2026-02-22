from itertools import permutations

# Problem 24: Find the millionth lexicographic permutation of 0-9
digits = list(range(10))
result = sorted(permutations(digits))[999999]
print("".join(map(str, result)))