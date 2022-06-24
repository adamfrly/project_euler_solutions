# Print the sum of all numbers divisible by either 3 or 5 from 1 to 999

result = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        result = result + i

print(result)
