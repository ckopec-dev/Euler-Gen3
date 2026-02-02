#!/usr/bin/env python3
"""
4-Digit Palindrome Finder
Displays all possible palindromes with 4 digits (1000-9999)
"""

def is_palindrome(num):
    """Check if a number is a palindrome"""
    num_str = str(num)
    return num_str == num_str[::-1]

def find_all_4digit_palindromes():
    """Find all 4-digit palindromes"""
    palindromes = []
    
    # 4-digit numbers range from 1000 to 9999
    for num in range(1000, 10000):
        if is_palindrome(num):
            palindromes.append(num)
    
    return palindromes

def main():
    print("=" * 50)
    print("4-DIGIT PALINDROME FINDER")
    print("=" * 50)
    print()
    
    palindromes = find_all_4digit_palindromes()
    
    print(f"Total count: {len(palindromes)} palindromes\n")
    
    # Display palindromes in a formatted grid (10 per row)
    print("All 4-digit palindromes:")
    print("-" * 50)
    
    for i, palindrome in enumerate(palindromes, 1):
        print(f"{palindrome}", end="  ")
        if i % 10 == 0:
            print()  # New line after every 10 palindromes
    
    print("\n" + "=" * 50)
    
    # Show the pattern
    print("\nPattern observation:")
    print("4-digit palindromes have the form: ABBA")
    print("Where A can be 1-9 (first digit can't be 0)")
    print("And B can be 0-9")
    print(f"Total possible: 9 × 10 = 90 palindromes")

if __name__ == "__main__":
    main()