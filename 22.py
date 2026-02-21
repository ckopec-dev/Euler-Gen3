import urllib.request


with open("22.txt") as f: data = f.read()

# Parse names
names = sorted(name.strip('"') for name in data.split(','))

def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

total = sum(name_score(name) * (i + 1) for i, name in enumerate(names))
print(total)  # Answer: 871198282