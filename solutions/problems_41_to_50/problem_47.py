# Find the first our consecutive numbers to have four distinct prime factors
# Answer is the first of the four numbers

def prime_factorization(num):
    """
    Returns the prime factorization of num
    """
    prime_factors = []
    d = 2
    while d * d < num:
        while num % d == 0:
            prime_factors.append(int(d))
            num = num / d
        d = d + 1

    if num > 1:
        prime_factors.append(int(num))

    return prime_factors

num = 1
consecutive = 0

while consecutive < 4:
    num += 1
    factors = prime_factorization(num)
    unique = list(set(factors))
    if len(unique) >= 4:
        consecutive += 1
    else:
        consecutive = 0

print(num - 3)