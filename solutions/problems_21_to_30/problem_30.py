# Find the sum of all numbers that can be written as the sum of fifth powers of their digits

# Can't have any with more than 6 digits because 7*9^5 = 413,343 < 1,000,000
# Could probably tighten that upper bound much more, but this worked

def digit_sum(n):  
    sum = 0
    for digit in str(n): 
      sum += int(digit) ** 5
    return sum

nums = []
for n in range(1000001):
    if digit_sum(n) == n:
        nums.append(n)

nums.remove(0)
nums.remove(1)

print(nums, sum(nums))