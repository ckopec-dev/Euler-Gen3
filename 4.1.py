
from tqdm import tqdm 
import time

def is_palindrome(n: int) -> bool:
        s = str(n)
        return s == s[::-1]

def calc(digits):
        start_time = time.perf_counter()
        max_pal = 0
        best_pair = (0, 0)
        lo = 10 ** (digits - 1) 
        hi = 10 ** digits

        for i in tqdm(range(lo, hi)):
                for j in range(i, hi):  # start at i to avoid duplicate work
                        product = i * j
                        if product > max_pal and is_palindrome(product):
                                max_pal = product
                                best_pair = (i, j)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Executed in {elapsed_time:.4f} seconds")
        print("Largest palindrome:", max_pal)
        print("From numbers:", best_pair)

#calc(3)
# Executed in 0.0260 seconds
# Largest palindrome: 906609
# From numbers: (913, 993)

#calc(4)
# Executed in 1.3056 seconds
# Largest palindrome: 99000099
# From numbers: (9901, 9999)

#calc(5)
# Executed in 146.4529 seconds
# Largest palindrome: 9966006699
# From numbers: (99681, 99979)