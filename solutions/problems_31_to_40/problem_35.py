# How many circular primes are there below 1,000,000?
# Other than 2 and 5, all members of the list need to be made up of 1, 3, 7, and 9s

################### Bad attempt that didn't go anywhere #################
# import itertools

# result = [2, 3, 5, 7]
# nums = [1, 3, 7, 9]

# def left_shift(tup, n):
#     try:
#         n = n % len(tup)
#     except ZeroDivisionError:
#         return tuple()
#     return tup[n:] + tup[0:n]

# def tuple_to_int(tple):
#     return int(''.join(map(str, tple)))

# # If sum of all digits is divisible by 3, the entire number is, so can eliminate those
# two_digits = list(itertools.product(nums, nums))
# three_digits = list(itertools.product(nums, nums, nums))
# four_digits = list(itertools.product(nums, nums, nums, nums))
# five_digits = list(itertools.product(nums, nums, nums, nums, nums))
# six_digits = list(itertools.product(nums, nums, nums, nums, nums, nums))

# def check_digits(lst):
#     for num in lst:
#         for i in range(len(num)):
#             temp = tuple_to_int(left_shift(num, i))
#             print(temp)
#             if not is_prime(temp):
#                 lst.remove(num)
#                 break

# check_digits(two_digits)

# print(two_digits)
        
################### Second Attempt ###################
def is_prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

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


primes = primes_sieve(1000000)
result = []

for num in primes:
    circ_prime = True
    str_num = str(num)
    for i in range(len(str_num)):
        str_rotated_num = str_num[i:len(str_num)] + str_num[0:i]
        rotated_num = int(str_rotated_num)
        if not is_prime(rotated_num):
            circ_prime = False
    if circ_prime:
        result.append(num)

print(len(result), result)
    