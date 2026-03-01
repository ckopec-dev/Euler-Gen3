from itertools import permutations

def solve():
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    
    for perm in permutations('0123456789'):
        if perm[0] == '0':
            continue
        digits = list(perm)
        
        valid = True
        for i, p in enumerate(primes):
            num = int(''.join(digits[i+1:i+4]))
            if num % p != 0:
                valid = False
                break
        
        if valid:
            n = int(''.join(digits))
            total += n
            print(n)
    
    print(f"\nAnswer: {total}")

solve()