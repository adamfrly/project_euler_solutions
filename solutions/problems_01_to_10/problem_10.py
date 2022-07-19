def is_prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

sum = 0
maximum = 2000000
for i in range(1, maximum + 1):
    if is_prime(i):
        sum = sum + i

print(sum)