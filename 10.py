
def sum_of_primes(limit):
    # Sieve of Eratosthenes
    sieve = bytearray([1]) * limit
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

result = sum_of_primes(2_000_000)
print(f"Sum of all primes below 2,000,000: {result}")