# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def primes_sieve(limit):
    """
    Lists all prime numbers less than the limit
    """
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

primes = primes_sieve(500000)

for i in range(9, 500001, 2):
    for j in range(1, i):
        found = True
        if (i - 2 * j * j) in primes:
            found = False
        if found:
            print(i)