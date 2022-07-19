# Find the largest palindromic product of two three digit numbers

def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + (n % 10)
        n = n // 10
    return reversed

def isPalidrome(n):
    return n == reverse(n)

result = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if isPalidrome(product) and product > result:
            result = product

print(result)
