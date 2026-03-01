MOD = 10**10
result = sum(pow(i, i, MOD) for i in range(1, 1001)) % MOD
print(result)  # 9110846700