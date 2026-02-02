from tqdm import tqdm 
import time

def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def calc(digits):
        start_time = time.perf_counter()
        max_pal = 0
        best_pair = (0, 0)
        lo = (10 ** (digits - 1)) - 1
        hi = (10 ** digits) - 1

        for i in tqdm(range(hi, lo, -1)):
                if i * hi < max_pal:
                        break  # no larger product possible
                for j in range(hi, i - 1, -1):
                        product = i * j
                        if product <= max_pal:
                                break
                        if is_palindrome(product):
                                max_pal = product
                                best_pair = (i, j)
                                break  # no need to check smaller j for this i

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Executed in {elapsed_time:.4f} seconds")
        print("Largest palindrome:", max_pal)
        print("From numbers:", best_pair)

#calc(3)
# Executed in 0.0006 seconds
# Largest palindrome: 906609
# From numbers: (913, 993)

#calc(4)
# Executed in 0.0008 seconds
# Largest palindrome: 99000099
# From numbers: (9901, 9999)

#calc(5)
# Executed in 0.0102 seconds
# Largest palindrome: 9966006699
# From numbers: (99681, 99979)
