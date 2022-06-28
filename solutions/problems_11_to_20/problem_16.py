# Find the sum of the digits of 2^1000

num = 2 ** 1000

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

print(sum_digits(num))
