# Find all the smallest positive integer that is evenly divisible by all numbers from 1 to 20


# Brute Forece attempt that ran for far too long
# 
# finished = False
# i = 1
# while not finished:
#     print(i)
#     trial = True
#     for j in range(1, 21):
#         if i % j != 0:
#             trial = False

#     if trial:
#         finished = True
#         result = i
#     else:
#         i = i + 1

# print("Final Result: ", result)

# Faster approach is to use the lcm. The desired number is just the lcm of the numbers 1-20
from functools import reduce

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_n(nums):
    return reduce(lcm, nums)

print(lcm_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        
