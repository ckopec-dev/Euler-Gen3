# Project Euler Problem 36
# Find the sum of all numbers less than one million which are palindromic in both base 10 and base 2

def is_palindrome(s):
    return s == s[::-1]

total = sum(
    n for n in range(1, 1_000_000)
    if is_palindrome(str(n)) and is_palindrome(bin(n)[2:])
)

print(f"Sum: {total}")