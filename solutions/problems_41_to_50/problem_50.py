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


n = 1000000
primes = []
i = 2
while sum(primes) < n:
    if is_prime(i):
        primes.append(i)
    i = i+1
fin_seq = []
l = len(primes)
j = l
while j != 0:
    i = 0
    while i+j < l+1:
        seq = primes[i:i+j]
        if sum(seq) <= n:
            if is_prime(sum(seq)):
                if len(seq) > len(fin_seq):
                    fin_seq = seq
        i = i+1
    j = j-1

print(fin_seq, sum(fin_seq))
