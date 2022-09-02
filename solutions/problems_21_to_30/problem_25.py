# Find the index of the first 1000 digit Fibonacci number
import math

def fibonacci(n):
    # Brute force
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_dp(n):
    # With Dynamic Programming
     
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

def fibo(n):
    # Using the fact that F_n = round(phi^n/sqrt(5))
    phi = (1 + math.sqrt(5)) / 2
 
    return round(pow(phi, n) / math.sqrt(5))

num = 0
i = 0
while len(str(num)) < 1000:
    i = i + 1
    num = fibonacci_dp(i)
    

print("Index: ", i, "Num: ", num)