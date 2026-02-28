# Build Champernowne's sequence until we have 1,000,000+ digits
s = ""
n = 1
while len(s) < 1_000_001:
    s += str(n)
    n += 1

product = 1
for i in range(7):        # 10^0 through 10^6
    idx = 10**i - 1       # convert to 0-based index
    digit = int(s[idx])
    product *= digit
    print(f"d(10^{i}) = d({10**i:>7}) = {digit}")

print(f"\nAnswer: {product}")