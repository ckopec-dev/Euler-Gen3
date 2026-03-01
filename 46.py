import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def satisfies_goldbach(n):
    for k in range(1, int(math.sqrt(n / 2)) + 1):
        remainder = n - 2 * k * k
        if remainder > 0 and is_prime(remainder):
            return True
    return False

n = 9
while True:
    if not is_prime(n) and n % 2 == 1:
        if not satisfies_goldbach(n):
            print(f"Answer: {n}")  # 5777
            break
    n += 2