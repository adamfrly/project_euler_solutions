# How many, not necessarily distinct, values of nCr for n in [1, 100], are greater than one-million?

from math import comb

count = 0
for n in range(1, 101):
    for r in range(1, 101):
        combo = comb(n,r)
        if combo > 1000000:
            count = count + 1

print(count)