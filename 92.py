# Project Euler Problem 92: Square Digit Chains

def square_digit_chain(n):
    """Calculate the next number in the square digit chain."""
    return sum(int(digit) ** 2 for digit in str(n))

def count_89_chains(limit):
    """Count how many starting numbers below `limit` arrive at 89."""
    cache = {}
    count = 0

    for i in range(1, limit):
        current = i
        chain = []

        while current != 1 and current != 89:
            if current in cache:
                current = cache[current]
                break
            chain.append(current)
            current = square_digit_chain(current)

        result = current
        for number in chain:
            cache[number] = result

        if result == 89:
            count += 1

    return count

if __name__ == "__main__":
    limit = 10_000_000
    result = count_89_chains(limit)
    print(f"The number of starting numbers below {limit} that arrive at 89 is: {result}")