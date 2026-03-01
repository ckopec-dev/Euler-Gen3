fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def next_n(x):
    return sum(fact[int(d)] for d in str(x))

cache = {}

def chain_length(n):
    chain = []
    visited = {}
    x = n
    while x not in visited and x not in cache:
        visited[x] = len(chain)
        chain.append(x)
        x = next_n(x)
    
    if x in cache:
        base = cache[x]
        for i, num in enumerate(reversed(chain)):
            cache[num] = base + i + 1
    else:
        # cycle found
        cycle_len = len(chain) - visited[x]
        for i in range(visited[x], len(chain)):
            cache[chain[i]] = cycle_len
        for i in range(visited[x] - 1, -1, -1):
            cache[chain[i]] = cache[chain[i + 1]] + 1

    return cache[n]

count = sum(1 for i in range(1, 1_000_000) if chain_length(i) == 60)
print(count)  # 402