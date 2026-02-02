#!/usr/bin/env python3
"""
5-Digit Palindrome Finder
"""

def is_palindrome(num):
    """Check if a number is a palindrome"""
    num_str = str(num)
    return num_str == num_str[::-1]

def find_all_5digit_palindromes():
    """Find all 5-digit palindromes"""
    palindromes = []
    
    for num in range(10000, 100000):
        if is_palindrome(num):
            palindromes.append(num)
    
    return palindromes

def main():
    print("=" * 50)
    print("5-DIGIT PALINDROME FINDER")
    print("=" * 50)
    print()
    
    palindromes = find_all_5digit_palindromes()
    
    print(f"Total count: {len(palindromes)} palindromes\n")
    
    # Display palindromes in a formatted grid (10 per row)
    print("All 5-digit palindromes:")
    print("-" * 50)
    
    for i, palindrome in enumerate(palindromes, 1):
        print(f"{palindrome}", end="  ")
        if i % 10 == 0:
            print()  # New line after every 10 palindromes
    
    print("\n" + "=" * 50)
    
if __name__ == "__main__":
    main()