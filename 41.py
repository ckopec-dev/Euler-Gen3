from itertools import permutations

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

# A pandigital number uses each digit 1-n exactly once.
# Key insight: sum of digits 1+2+...+n must not be divisible by 3 for prime candidates
# 1+2+...+9 = 45 (div by 3), 1..8 = 36 (div by 3), 1..7 = 28 (not div by 3)
# So the largest pandigital prime can be at most 7 digits

largest = 0
for n in range(7, 0, -1):
    digits = list(range(n, 0, -1))  # descending for largest first
    for perm in permutations(digits):
        num = int(''.join(map(str, perm)))
        if is_prime(num) and num > largest:
            largest = num
    if largest > 0:
        break

print(f"Answer: {largest}")  # 7652413