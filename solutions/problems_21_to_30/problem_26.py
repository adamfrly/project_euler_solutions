# Find d < 1000 that gives the longest cycle of repeating digits for 1 / d

# Reciprical period length is always a factor of the totient of the denominator
# The totient is the number of positive integers not greater than the integer which are realatively prime with it
# This means it's most likely going to be a prime number

######## Potential solution from stack overflow, ended up being over complicated ###############
# def gcd(a, b):
#     if (a == 0):
#         return b
#     return gcd(b % a, a)

# def totient(n):
#     result = 1
#     for i in range(2, n):
#         if (gcd(i, n) == 1):
#             result += 1
#     return result

def period(x):
    seen_remainders = [0] * x
    value = 1
    count = 0
    while seen_remainders[value] == 0 and value != 0:
        seen_remainders[value] = count
        value = value * 10
        value = value % x
        count = count + 1
    
    return count - seen_remainders[value]

periods = [period(x) for x in range(2,1001)]

print(max(periods), periods.index(max(periods)) + 2)

