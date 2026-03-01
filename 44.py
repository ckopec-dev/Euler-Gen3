def pent(n):
    return n * (3*n - 1) // 2

def is_pent(x):
    import math
    d = 1 + 24*x
    s = int(math.isqrt(d))
    if s*s != d:
        return False
    return (1 + s) % 6 == 0

pent_list = []
k = 1
while True:
    pk = pent(k)
    for j in range(k-1, 0, -1):
        pj = pent_list[j-1]
        diff = pk - pj
        if is_pent(diff) and is_pent(pk + pj):
            print(f"Answer: D = {diff}")
            exit()
    pent_list.append(pk)
    k += 1