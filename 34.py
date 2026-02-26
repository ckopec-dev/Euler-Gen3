from math import factorial

result = sum(
    n for n in range(3, 2_540_161)
    if sum(factorial(int(d)) for d in str(n)) == n
)
print(result)  # 40730