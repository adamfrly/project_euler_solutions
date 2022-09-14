# If dn represents the nth digit of the fractional part of 0.123456789101112131415161718192021...
# 
# Find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
from math import prod

fractional = "".join(str(i) for i in range(1, 10000000))

digits = []
for n in range(7):
    digits.append(int(fractional[10 ** n - 1]))

print(prod(digits))