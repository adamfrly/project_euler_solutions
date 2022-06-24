# Find the difference between the sum of sqaures and square of sums of numbers between 1-100
# Find (1 + 2 + ... + 100)^2 - (1^2 + 2^2 + ... + 100^2)

def sum_of_nums(start, end):
    return (end - start + 1) * (end + start) / 2

square_of_sums = sum_of_nums(1, 100) ** 2

sum_of_squares = 0
for i in range(1, 101):
    sum_of_squares = sum_of_squares + (i ** 2)

print(square_of_sums - sum_of_squares)
