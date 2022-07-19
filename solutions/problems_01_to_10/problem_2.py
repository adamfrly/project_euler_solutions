# Print the sum of all even fibonacci numbers less than 4,000,000

result = 2

fib_1 = 1
fib_2 = 2

total = 0

while total < 4000000:
    total = fib_1 + fib_2
    if total % 2 == 0:
        result = result + total

    fib_1 = fib_2
    fib_2 = total

print(result)