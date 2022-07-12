# Find d < 1000 that gives the longest cycle of repeating digits for 1 / d

# Reciprical period length is always a factor of the totient of the denominator
# The totient is the number of positive integers not greater than the integer which are realatively prime with it
# This means it's most likely going to be a prime number

def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)

def totient(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result

print(totient(6173))
