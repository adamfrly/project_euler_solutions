# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def factorial(x: int) -> int:
    total = 1
    for i in range(0, x):
        total = total * (i + 1)
    return total

def sfd(x: int) -> int:
    total = 0
    while x > 0:
        total = total + factorial(x % 10)
        x = x // 10
    return total


results = []

for i in range(100000):
    if sfd(i) == i:
        results.append(i)

results.remove(0)
results.remove(1)
results.remove(2)

print(sum(results))