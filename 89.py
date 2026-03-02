"""
Project Euler - Problem 89: Roman numerals

Each Roman numeral can be written in a minimal form using subtractive notation
(e.g. "IX" instead of "VIIII"). Given a file containing one thousand valid
Roman numerals (not necessarily minimal), determine the total number of
characters saved by writing each numeral in its minimal form.

The accompanying data file `089.txt` contains the input numerals.

Answer: 743 (verified)
"""

# mapping of single Roman digits to their integer values
VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# ordered list of (value, numeral) pairs for constructing minimal forms
MINIMAL = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to an integer value."""
    total = 0
    i = 0
    while i < len(s):
        # peek at next character to handle subtractive pairs
        if i + 1 < len(s) and VALUES[s[i]] < VALUES[s[i + 1]]:
            total += VALUES[s[i + 1]] - VALUES[s[i]]
            i += 2
        else:
            total += VALUES[s[i]]
            i += 1
    return total


def int_to_minimal_roman(n: int) -> str:
    """Construct the minimal Roman numeral for integer ``n`` (1 <= n <= 3999).

    The input range of the problem may actually generate numerals up to 4999
    because of the original non-minimal forms, but the greedy algorithm still
    works in that domain since "MMMM" is allowed.
    """
    result = []
    for value, numeral in MINIMAL:
        while n >= value:
            result.append(numeral)
            n -= value
    return ''.join(result)


def solve() -> int:
    # read the data file which should be in the same directory
    try:
        with open('089.txt') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise RuntimeError("Data file '089.txt' not found in the working directory")

    saved = 0
    for roman in lines:
        original_len = len(roman)
        value = roman_to_int(roman)
        minimal = int_to_minimal_roman(value)
        saved += original_len - len(minimal)
    return saved


if __name__ == '__main__':
    answer = solve()
    print(f"Answer: {answer}")  # 743
