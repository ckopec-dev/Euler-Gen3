def sieve(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return is_prime

LIMIT = 1_000_000
is_prime = sieve(LIMIT)
primes = [i for i in range(2, LIMIT) if is_prime[i]]

# Build prefix sums for efficient range summing
prefix = [0] * (len(primes) + 1)
for i, p in enumerate(primes):
    prefix[i+1] = prefix[i] + p
    if prefix[i+1] >= LIMIT:
        max_len = i+1
        break

best_len = 0
best_prime = 0

for start in range(max_len):
    for end in range(start + best_len + 1, max_len + 1):
        s = prefix[end] - prefix[start]
        if s >= LIMIT:
            break
        if is_prime[s] and (end - start) > best_len:
            best_len = end - start
            best_prime = s

print(f'Answer: {best_prime}')        # 997651
print(f'Consecutive primes: {best_len}')  # 543