"""
Project Euler - Problem 88: Product-Sum Numbers

A natural number N that can be written as both the sum and product
of a given set of at least two natural numbers is called a product-sum number.

Find the sum of all minimal product-sum numbers for 2 <= k <= 12000.

Key insight:
  For any factorization of N with f factors and factor-sum s,
  we can pad with (N - s) ones to get k = f + (N - s) total terms
  where both the sum and product equal N.

Answer: 7587457
"""

def solve():
    limit = 12001

    # min_n[k] = minimal product-sum number for a given k
    min_n = [float('inf')] * limit

    def search(product, total, factors, start):
        # How many terms needed if we pad the rest with 1s?
        # Adding (product - total) ones makes sum == product
        k = factors + product - total
        if k < limit:
            if product < min_n[k]:
                min_n[k] = product

        # Extend the factorization with another factor >= start
        for f in range(start, limit):
            if product * f > limit * 2:
                break
            search(product * f, total + f, factors + 1, f)

    # Start with an implicit factor of 1 (product=1, sum=1, factors=1)
    search(1, 1, 1, 2)

    # Sum distinct minimal product-sum numbers for k in [2, 12000]
    return sum(set(min_n[2:limit]))


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")  # 7587457