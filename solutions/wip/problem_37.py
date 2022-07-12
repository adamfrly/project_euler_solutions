# Find the sum of all 11 numbers that are trunctable primes
from utils import is_prime

prime_count = 0

candidates = []
numbers = [3, 7, 9]

def find_trunct(num):
    if is_prime(num):
        for new_num in numbers:
            find_trunct(int(str(num) + str(new_num)))
    else:
        candidates.append(num)
        return num
    