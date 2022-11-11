# Find the largest prime pandigital number

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

primes = primes_sieve(100000000) # 100000000

for prime in primes:
    digits = len(str(prime))
    prime_list = [int(x) for x in str(prime)]
    prime_list.sort()
    if prime_list == list(range(1, digits + 1)):
        print(prime)