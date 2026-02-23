"""
Euler Problem 31: Coin Sums

In England the currency is made up of pound and pence, and there are
eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

How many different ways can £2 be made using any number of coins?
"""

def solve():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    # dp[i] = number of ways to make amount i
    dp = [0] * (target + 1)
    dp[0] = 1  # one way to make 0: use no coins

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]

print(f"Answer: {solve()}")