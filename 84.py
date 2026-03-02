"""
Project Euler Problem 84: Monopoly Odds

In the game of Monopoly, the standard board is set up with squares numbered 0-39.
Using a 4-sided dice, find the three most popular squares and give the answer
as a 6-digit modal string.

Board layout:
GO=0, A1=1, CC1=2, A2=3, T1=4, R1=5, B1=6, CH1=7, B2=8, B3=9,
JAIL=10, C1=11, U1=12, C2=13, C3=14, R2=15, D1=16, CC2=17, D2=18, D3=19,
FP=20, E1=21, CH2=22, E2=23, E3=24, R3=25, F1=26, F2=27, U2=28, F3=29,
G2J=30, G1=31, G2=32, CC3=33, G3=34, R4=35, CH3=36, H1=37, T2=38, H2=39

Special squares:
- G2J (30): Go to Jail -> land on 10
- CC (2, 17, 33): Community Chest - 1/16 go to GO, 1/16 go to JAIL, 14/16 stay
- CH (7, 22, 36): Chance - go to specific squares (8 cards), or stay
- If doubles 3 times in a row: go to jail
"""

import random
from collections import defaultdict

def simulate_monopoly(dice_sides=4, num_rolls=1_000_000):
    # Square indices
    GO, JAIL, G2J = 0, 10, 30
    CC = {2, 17, 33}
    CH = {7, 22, 36}
    R = [5, 15, 25, 35]  # Railroads
    U = [12, 28]          # Utilities
    
    counts = defaultdict(int)
    pos = 0
    doubles_count = 0
    
    for _ in range(num_rolls):
        d1 = random.randint(1, dice_sides)
        d2 = random.randint(1, dice_sides)
        roll = d1 + d2
        
        if d1 == d2:
            doubles_count += 1
            if doubles_count == 3:
                pos = JAIL
                doubles_count = 0
                counts[pos] += 1
                continue
        else:
            doubles_count = 0
        
        pos = (pos + roll) % 40
        
        # G2J
        if pos == G2J:
            pos = JAIL
        
        # Community Chest
        elif pos in CC:
            card = random.randint(1, 16)
            if card == 1:
                pos = GO
            elif card == 2:
                pos = JAIL
        
        # Chance
        elif pos in CH:
            card = random.randint(1, 16)
            if card == 1:
                pos = GO
            elif card == 2:
                pos = JAIL
            elif card == 3:
                pos = 11  # C1
            elif card == 4:
                pos = 24  # E3
            elif card == 5:
                pos = 39  # H2
            elif card == 6:
                pos = 5   # R1
            elif card in (7, 8):  # next railroad
                for r in R:
                    if r > pos:
                        pos = r
                        break
                else:
                    pos = R[0]
            elif card == 9:  # next utility
                for u in U:
                    if u > pos:
                        pos = u
                        break
                else:
                    pos = U[0]
            elif card == 10:  # go back 3
                pos = (pos - 3) % 40
                # Check if landed on CC3 after going back
                if pos in CC:
                    c2 = random.randint(1, 16)
                    if c2 == 1:
                        pos = GO
                    elif c2 == 2:
                        pos = JAIL
        
        counts[pos] += 1
    
    return counts

random.seed(42)
counts = simulate_monopoly(dice_sides=4, num_rolls=2_000_000)

sorted_squares = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print("Top 10 most visited squares:")
total = sum(counts.values())
for sq, cnt in sorted_squares[:10]:
    print(f"  Square {sq:02d}: {cnt} visits ({100*cnt/total:.2f}%)")

top3 = [sq for sq, _ in sorted_squares[:3]]
answer = "".join(f"{sq:02d}" for sq in top3)
print(f"\nAnswer (modal string): {answer}")