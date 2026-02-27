def solve():
    from sympy import isprime
    
    def get_rotations(n):
        s = str(n)
        return [int(s[i:] + s[:i]) for i in range(len(s))]
    
    count = 0
    for n in range(2, 1_000_000):
        if all(isprime(r) for r in get_rotations(n)):
            count += 1
    
    return count

print(solve())