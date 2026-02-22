"""
Project Euler Problem 25:
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def solve():
    a, b = 1, 1
    index = 2
    while len(str(b)) < 1000:
        a, b = b, a + b
        index += 1
    return index

print(solve())  # Answer: 4782