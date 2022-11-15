# Find how many chains, with a starting number below one million, contain exactly sixty non-repeating terms.
# Sequence is defined as taking the sum of the factorial of the digits of the preceding number.

# Originally did it brute force, but applied caching after. Cahching didn't actually make it that much faster

from math import factorial

def sum_of_factorial_digits(n):
    return sum([factorial(int(x)) for x in str(n)])

result = []
seen = {169: 3, 363601: 3, 1454: 3, 871: 2, 872: 2, 45361: 2, 45362: 2}

for i in range(1,1000000):
    seq = []
    flag = True
    n = i
    length = 0
    falg = True
    while n not in seq and flag:
        if n in seen:
            length += seen[n]
            flag = False
        if flag:
            seq.append(n)
            n = sum_of_factorial_digits(n)
    length += len(seq)
    if length == 60:
        result.append(i)

print(result, len(result))
