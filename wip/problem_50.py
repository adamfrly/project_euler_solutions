# Find the longest sequence of consecutive primes under 1,000,000 that sums to another prime

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

primes = primes_sieve(100)
candidate = []
result = 0
max_length = 0

for start in primes:
    cand_start = start
    candidate = []
    length = 0
    for num in primes[primes.index(start):]:
        candidate.append(num)
        if is_prime(sum(candidate)):
            if len(candidate) > length:
                length = len(candidate)
    if length > max_length:
        max_length = length
        result = cand_start

print(max_length, result)
