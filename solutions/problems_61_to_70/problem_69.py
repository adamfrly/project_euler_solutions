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

maximum = 0
index = -1

for i in range(2, 1000001):
    phi_i = i / phi(i)
    if phi_i > maximum:
        maximum = phi_i
        index = i

print(index, maximum)
