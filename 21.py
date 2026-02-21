def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def solve():
    total = 0
    for a in range(2, 10000):
        b = sum_of_divisors(a)
        if b != a and sum_of_divisors(b) == a:
            total += a
    return total

print(solve())  # 31626