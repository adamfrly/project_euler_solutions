# Find the 10001st prime number

def is_prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

def nth_prime(n):
    count = 0
    i = 0
    while count <= (n - 1):
        i = i + 1
        if is_prime(i):
            count = count + 1
    return i

print(nth_prime(10001))