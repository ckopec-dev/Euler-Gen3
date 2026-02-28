largest = 0

for x in range(1, 10000):
    concat = ""
    for n in range(1, 10):
        concat += str(x * n)
        if len(concat) >= 9:
            if len(concat) == 9 and set(concat) == set("123456789"):
                largest = max(largest, int(concat))
            break

print(f"Answer: {largest}")  # 932718654