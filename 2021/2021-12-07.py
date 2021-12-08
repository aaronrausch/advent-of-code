
with open('inputs/2021-12-07.txt') as f:
    d = [int(n) for n in f.read().split(',')]
    MIN, MAX = min(d), max(d)

def naturals(x): return (x * (x + 1)) // 2

m = float("inf")
for pos in range(MIN, MAX):
    fuel = sum(abs(c - pos) for c in d)
    m = min(fuel, m)
print(m)

m = float("inf")
for pos in range(MIN, MAX):
    fuel = sum(naturals(abs(c - pos)) for c in d)
    m = min(fuel, m)
print(m)
