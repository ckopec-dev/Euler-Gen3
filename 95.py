# Solution for Project Euler Problem 95
# Problem Statement: Find the smallest member of the longest amicable chain with no element exceeding one million.

def sum_of_divisors(n):
    """Returns the sum of proper divisors of n."""
    total = 1
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def find_amicable_chain(limit):
    """Finds the smallest member of the longest amicable chain under the given limit."""
    divisor_sums = [0] * (limit + 1)
    for i in range(1, limit + 1):
        divisor_sums[i] = sum_of_divisors(i)

    visited = [False] * (limit + 1)
    longest_chain = []

    for i in range(1, limit + 1):
        if visited[i]:
            continue

        chain = []
        current = i
        while current <= limit and not visited[current]:
            visited[current] = True
            chain.append(current)
            current = divisor_sums[current]

            if current in chain:
                cycle_start = chain.index(current)
                cycle = chain[cycle_start:]
                if len(cycle) > len(longest_chain):
                    longest_chain = cycle
                break

    return min(longest_chain) if longest_chain else None

if __name__ == "__main__":
    LIMIT = 10**6
    result = find_amicable_chain(LIMIT)
    print("The smallest member of the longest amicable chain is:", result)