from itertools import combinations


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

for prime in primes:
    prime_perms = list(combinations(list(str(prime))))
    results = []
    for perm in prime_perms:
        candidate = int("".join(perm))
        if is_prime(candidate) and len(str(candidate)) == 4:
            results.append(candidate)
            
    if len(results) >= 3:
        print(results)

