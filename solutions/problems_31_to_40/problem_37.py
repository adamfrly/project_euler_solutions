# Find the sum of all 11 numbers that are trunctable primes

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

prime_count = 0

candidates_r = []
candidates_l = []
final_cands = []
numbers = [1, 2, 5, 3, 7, 9]

def find_trunct_r(num):
    if is_prime(num):
        for new_num in numbers:
            find_trunct_r(int(str(num) + str(new_num)))
        candidates_r.append(num)
    return num

def find_trunct_l(num):
    if is_prime(num):
        for new_num in numbers:
            find_trunct_l(int(str(new_num) + str(num)))
        candidates_l.append(num)
    return num

for num in numbers:
    find_trunct_r(num)
    find_trunct_l(num)

for num in candidates_l:
    if num in candidates_r and is_prime(num):
        final_cands.append(num)

print(sum(final_cands) - (2 + 3 + 5 + 7))