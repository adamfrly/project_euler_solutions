# A bunch of utility functions for basic tasks that keep reoccuirng in problems

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

def prime_factorization(num):
    """
    Returns the prime factorization of num
    """
    prime_factors = []
    d = 2
    while d * d < num:
        while num % d == 0:
            prime_factors.append(d)
            num = num / d
        d = d + 1

    if num > 1:
        prime_factors.append(num)

    return prime_factors

def gcd(a, b):
    """
    Returns the gcd of number a and b
    """
    if (a == 0):
        return b
    return gcd(b % a, a)

def lcm(a, b):
    """
    Returns the lcd of numbers a and b
    """
    return a * b // gcd(a, b)

def divisors(n, include_n = False):
    """
    Returns the divisors of a number. Can opt to remove n from the list 
    """
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            result.append(n//i)
    if not include_n:
        result.remove(n)
    return result

def factorial(x: int) -> int:
    """
    Returns the factorial of x
    """
    total = 1
    for i in range(0, x):
        total = total * (i + 1)
    return total

def sfd(x: int, b: int) -> int:
    """
    Returns the sum of the factorial of the digits in base b.
    """
    total = 0
    while x > 0:
        total = total + factorial(x % b)
        x = x // b
    return total