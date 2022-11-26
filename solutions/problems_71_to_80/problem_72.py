# How many reduced proper fractions are there when the denominator is <= 1,000,000

def phi(n):
    phi = int(n > 1 and n)
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1: phi -= phi // n 
    return phi


nums = [phi(x) for x in range(1, 1000001)]

print(sum(nums))