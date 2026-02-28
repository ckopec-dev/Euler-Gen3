from collections import defaultdict

counts = defaultdict(int)

for a in range(1, 1000):
    for b in range(a, 1000):  # b >= a to avoid duplicates
        c_sq = a*a + b*b
        c = int(c_sq**0.5)
        if c*c == c_sq:       # check if c is a perfect square
            p = a + b + c
            if p <= 1000:
                counts[p] += 1

answer = max(counts, key=counts.get)
print(answer)
# p = 840, solutions = 8