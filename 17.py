"""
Euler Problem 17: Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3+3+5+4+4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens.
"""

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def number_to_words(n):
    if n == 1000:
        return "onethousand"
    elif n >= 100:
        hundreds = ones[n // 100] + "hundred"
        remainder = n % 100
        if remainder == 0:
            return hundreds
        else:
            return hundreds + "and" + number_to_words(remainder)
    elif n >= 20:
        return tens[n // 10] + ones[n % 10]
    else:
        return ones[n]

total = sum(len(number_to_words(n)) for n in range(1, 1001))
print(f"Total letters used: {total}")