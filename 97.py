# Problem 97: Large non-Mersenne prime
# The task is to find the last ten digits of the non-Mersenne prime: 28433 × 2^7830457 + 1

def solve_euler_97():
    base = 2
    exponent = 7830457
    multiplier = 28433
    addition = 1
    mod = 10**10  # We only care about the last 10 digits

    # Calculate the modular exponentiation
    result = pow(base, exponent, mod)

    # Multiply by the multiplier, add 1, and take modulo again
    result = (result * multiplier + addition) % mod

    return result

if __name__ == "__main__":
    print("The last ten digits of the large non-Mersenne prime are:", solve_euler_97())