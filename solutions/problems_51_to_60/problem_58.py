# Find how many rings of spiral numbers it takes before less
# than 10% of the number on the diagonals are prime

# Most of this code is pulled from question 28

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

size = 27501
count = 1
n = 1
num_primes = 0
for i in range(2, size, 2):
    for j in range(4):
        n += i
        if is_prime(n):
            num_primes += 1
        count += 1
    print(f"{i // 2}th ring", num_primes, count, num_primes/count)

# Ring number should be x2 and +1 to get side length (what the question is asking for)