# Shot in the dark wolfram alpha method
from math import sqrt

# This is some wolfram alpha and desmos dark magic
# Used https://www.wolframalpha.com/input?i=N%5E2-N+%3D+2%28n%5E2-n%29, plugged third integer solution into desmos and found that when m = 17, N crosses 10^12
# Equation comes from requirement that n/N*(n-1)/(N-1) = 1/2
m = 17
n = (2 * (3 - 2 * sqrt(2)) ** m + sqrt(2) * (3 - 2 * sqrt(2)) ** m + 2 * (3 + 2 * sqrt(2)) ** m - sqrt(2) * (3 + 2 * sqrt(2)) ** m + 4) / 8
N = (-(3-2 * sqrt(2)) ** m-sqrt(2)*(3-2 * sqrt(2)) ** m-(3+2 * sqrt(2)) ** m+sqrt(2)*(3+2 * sqrt(2)) ** m+2) / 4

# These print non integer numbers, but when rounded to the nearest integer you get the right answer. Probably precision/floating point error I assume
print("N: {:.25f}".format(N))
print("n: {:.25f}".format(n))


print(n/N*(n-1)/(N-1)) # Approximation is very close

print(756872327473/1070379110497*(756872327473-1)/(1070379110497-1)) # Plugging in closest numbers

# Apparently this is meant to be a diophantine equation problem lol