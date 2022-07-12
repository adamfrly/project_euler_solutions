# Find the values of a < 1000 and b <= 1000 that gives the makes the quadratic n^2 + an + b produce the largest string of consectuive prime numbers from n = 0 to n = a

def primes_sieve(limit):
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
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


# Going to do a brute force search, but with some restrictions. Plugging n = 0 shows that b must be prime, and n = 1, shows 1 + a + b must be prime,
# therefore a must be odd (unless b = 2, but I'm assuming it won't be)

primes_no_neg = primes_sieve(1000)
primes = []
for num in primes_no_neg:
    primes.append(num)
    primes.append(-1 * num)
    primes.sort()

n_max = 0
a_max = 0
b_max = 0
for b in primes:
    for a in range(-999, 1000, 2):
        n = 0
        while is_prime(abs(n ** 2 + a * n + b)):
            n = n + 1
        if n > n_max:
            n_max = n
            a_max = a
            b_max = b

print("Maximizing coefficients: ", a_max, b_max, "Sequence length: ", n_max)
print(a_max * b_max)
