import math

# Euler Problem 20: Factorial digit sum
# Find the sum of the digits in 100!

result = sum(int(d) for d in str(math.factorial(100)))
print(f"100! = {math.factorial(100)}")
print(f"Sum of digits in 100! = {result}")