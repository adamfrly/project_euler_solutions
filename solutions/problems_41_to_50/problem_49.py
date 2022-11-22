from itertools import permutations


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

def is_prime(n):
    """
    Checks if n is a prime number
    """
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

primes = primes_sieve(9999)

primes = list(filter(lambda prime: prime >= 1000, primes))

for prime in primes:
    prime_perms = [int("".join(x)) for x  in list(permutations(list(str(prime))))]
    prime_1 = prime + 3330
    prime_2 = prime + 6660
    if is_prime(prime_1) and is_prime(prime_2) and prime_1 in prime_perms and prime_2 in prime_perms:
        print(prime, prime_1, prime_2)

