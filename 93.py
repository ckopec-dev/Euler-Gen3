from itertools import permutations, product

def generate_expressions(numbers):
    operators = ['+', '-', '*', '/']
    expressions = set()

    for nums in permutations(numbers):
        for ops in product(operators, repeat=3):
            # Generate all possible parenthesized expressions
            exprs = [
                f"(({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}) {ops[2]} {nums[3]}",
                f"({nums[0]} {ops[0]} ({nums[1]} {ops[1]} {nums[2]})) {ops[2]} {nums[3]}",
                f"{nums[0]} {ops[0]} (({nums[1]} {ops[1]} {nums[2]}) {ops[2]} {nums[3]})",
                f"{nums[0]} {ops[0]} ({nums[1]} {ops[1]} ({nums[2]} {ops[2]} {nums[3]}))",
                f"({nums[0]} {ops[0]} {nums[1]}) {ops[1]} ({nums[2]} {ops[2]} {nums[3]})"
            ]

            expressions.update(exprs)

    return expressions

def evaluate_expression(expr):
    try:
        result = eval(expr)
        if result > 0 and result == int(result):
            return int(result)
    except ZeroDivisionError:
        pass
    return None

def find_longest_consecutive_set():
    max_consecutive = 0
    best_set = None

    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    numbers = [a, b, c, d]
                    expressions = generate_expressions(numbers)
                    results = set()

                    for expr in expressions:
                        result = evaluate_expression(expr)
                        if result is not None:
                            results.add(result)

                    # Find the longest consecutive sequence starting from 1
                    n = 1
                    while n in results:
                        n += 1

                    if n - 1 > max_consecutive:
                        max_consecutive = n - 1
                        best_set = numbers

    return best_set, max_consecutive

if __name__ == "__main__":
    best_set, max_consecutive = find_longest_consecutive_set()
    print(f"Best set: {best_set}, Longest consecutive: {max_consecutive}")