# Find the sum of digits of 100!

from math import factorial

num = factorial(100)

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

print(sum_digits(num))