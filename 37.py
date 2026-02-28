from sympy import isprime

def is_truncatable(n):
    s = str(n)
    for i in range(len(s)):
        if not isprime(int(s[i:])):   # truncate from left
            return False
        if not isprime(int(s[:i+1])): # truncate from right
            return False
    return True

results = []
n = 11
while len(results) < 11:
    if isprime(n) and is_truncatable(n):
        results.append(n)
    n += 2

print("Truncatable primes:", results)
print("Sum:", sum(results))