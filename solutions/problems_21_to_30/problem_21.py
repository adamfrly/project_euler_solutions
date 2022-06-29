# Find the sum of all amicable numbers from 1 to 1000

checked = []
ami = []

def divisors_no_n(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            result.append(n//i)
    result.remove(n)
    return result

def is_prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

for i in range(1, 10001):
    if i not in checked and not is_prime(i):
        da = sum(divisors_no_n(i))
        db = sum(divisors_no_n(da))
        checked.extend([da,db])
        if i == db:
            if da != db:
                ami.extend([i, da])

print(sum(ami))