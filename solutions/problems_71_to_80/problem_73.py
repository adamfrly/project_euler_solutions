# Find many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000
from math import gcd

limit = 12000
fracs = []

for n in range(1, limit + 1):
    for d in range(n, limit + 1):
        frac = n/d
        if gcd(n,d) == 1 and frac > 1/3 and frac < 1/2:
            fracs.append(f"{n}/{d}")

print(len(fracs))