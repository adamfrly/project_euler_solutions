# Find the sum of all positive integers which cannot be written as a sum of two abundant numbers

# All numbers above 20161 can be written as the sum of two abundant numbers https://oeis.org/A048242
# In this page, all even numbers above 46 can be expresses as the sum of two adundant numbers

# Any multiple of an abundant or perfect number is an abundant number


def divisors(n, include_n = False):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            result.append(n//i)
    if not include_n:
        result.remove(n)
    return list(set(result))

limit = 28125
abundant_nums = []
results = [False] * (limit + 10) # This 10 addition was completely arbitrarary and to accomodate an index out of bound error, but it's right :)
    
for i in range(1, limit):
    divs = divisors(i)
    sum_of_divisors = sum(divs)
    if sum_of_divisors > i:
        abundant_nums.append(i)


for n in abundant_nums:
    for m in abundant_nums:
        if n + m <= limit:
            results[n + m] = True

count = sum(i for i in range(limit) if not results[i])

print(count)
