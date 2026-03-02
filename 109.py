"""
Problem 109: Darts

In the game of darts, a player can score points by hitting specific regions.
An outer ring is a double and an inner ring is a triple.

We need to find the number of ways to score less than 100 with exactly 3 darts,
where the last dart must be a double.

So we need: score < 100, exactly 3 darts, last dart is double.
"""

def solve():
    # Possible single scores (1-20, 25)
    # Doubles: 2x for each single
    # Triples: 3x for each single (1-20 only)
    
    scores = set()
    
    # Singles (1-20, 25)
    for i in list(range(1, 21)) + [25]:
        scores.add(i)
        scores.add(2 * i)  # double
        if i <= 20:
            scores.add(3 * i)  # triple
    
    scores = sorted(list(scores))
    
    distinct_checkouts = set()
    
    # The last dart must be a double
    doubles = [2 * i for i in list(range(1, 21)) + [25]]
    
    for last_dart in doubles:
        if last_dart >= 100:
            continue
        
        # First and second darts (any score)
        for first_dart in scores:
            if first_dart + last_dart >= 100:
                continue
            for second_dart in scores:
                total = first_dart + second_dart + last_dart
                if 1 <= total < 100:
                    # Store as sorted tuple for first two darts (order doesn't matter)
                    combo = tuple(sorted([first_dart, second_dart]) + [last_dart])
                    distinct_checkouts.add(combo)
    
    return len(distinct_checkouts)

if __name__ == '__main__':
    result = solve()
    print(f"Answer: {result}")
