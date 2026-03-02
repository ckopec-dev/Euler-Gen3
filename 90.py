"""
Project Euler Problem 90: Cube Digit Pairs

Each of the six faces on two dice can have a digit (0-9) written on it.
The dice are rolled and the two resulting numbers are formed by the upper faces.
For example, if the dice show 6 and 4, then numbers 64 and 46 could be formed.

In how many ways can two sets of six different digits be chosen so that when
the dice are rolled, they can show all the two-digit representations of perfect squares:
01, 04, 09, 16, 25, 36, 49, 64, 81

Key: 6 and 9 are interchangeable (one can be rotated to look like the other)
"""

from itertools import combinations

def can_form_squares(die1, die2):
    """
    Check if two dice can form all required squares.
    die1 and die2 are tuples of digits (0-9)
    6 and 9 are interchangeable (can be rotated to look like each other)
    """
    # Required two-digit squares (all perfect squares from 1 to 81)
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
    
    set1 = set(die1)
    set2 = set(die2)
    
    for square in squares:
        d1, d2 = int(square[0]), int(square[1])
        
        # Check if we can form this square
        # For each digit, check if it's on a die (accounting for 6/9 equivalence)
        def has_digit(die_set, digit):
            if digit == 6:
                return 6 in die_set or 9 in die_set
            elif digit == 9:
                return 6 in die_set or 9 in die_set
            else:
                return digit in die_set
        
        # Can form square if: (d1 on die1 and d2 on die2) or (d1 on die2 and d2 on die1)
        can_form = (has_digit(set1, d1) and has_digit(set2, d2)) or \
                   (has_digit(set1, d2) and has_digit(set2, d1))
        
        if not can_form:
            return False
    
    return True

def solve():
    """
    Count valid unordered pairs of dice.
    """
    count = 0
    valid_pairs = set()  # Store pairs as sorted tuples to avoid duplicates
    digits = list(range(10))  # 0-9
    
    # Generate all combinations of 6 digits
    all_combos = list(combinations(digits, 6))
    
    # Check all pairs
    for die1 in all_combos:
        for die2 in all_combos:
            if can_form_squares(die1, die2):
                # Store as a sorted pair to count unordered pairs only once
                pair = tuple(sorted([die1, die2]))
                valid_pairs.add(pair)
    
    return len(valid_pairs)

if __name__ == "__main__":
    result = solve()
    print(f"Number of ways to arrange digits on two dice: {result}")
