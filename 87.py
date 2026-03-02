def sieve(limit):
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return [i for i, v in enumerate(is_prime) if v]

LIMIT = 50_000_000
primes = sieve(int(LIMIT**0.5) + 1)

results = set()
for p2 in primes:
    sq = p2 * p2
    if sq >= LIMIT: break
    for p3 in primes:
        cu = p3 ** 3
        if sq + cu >= LIMIT: break
        for p4 in primes:
            fo = p4 ** 4
            total = sq + cu + fo
            if total >= LIMIT: break
            results.add(total)

print(len(results))  # 1097343