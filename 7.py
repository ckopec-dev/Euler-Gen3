def solve():
    def is_prime(n):
        if n < 2: return False
        if n < 4: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    count, num = 0, 1
    while count < 10001:
        num += 1
        if is_prime(num):
            count += 1

    return num

print(solve())  # 104743