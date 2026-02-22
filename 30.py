# Euler Problem 30: Digit Fifth Powers
# Find the sum of all numbers that can be written as the sum of fifth powers of their digits.

# Upper bound: 9^5 = 59049, so a 7-digit number max is 7 * 59049 = 413343 (6 digits)
# 6 * 59049 = 354294, so numbers can't exceed 6 digits

result = sum(
    n for n in range(2, 6 * 9**5 + 1)
    if n == sum(int(d)**5 for d in str(n))
)

print(f"Numbers: {[n for n in range(2, 6 * 9**5 + 1) if n == sum(int(d)**5 for d in str(n))]}")
print(f"Answer: {result}")