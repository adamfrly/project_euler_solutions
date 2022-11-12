# Considering natural numbers of the form, ab, where a, b < 100, find the number with the maximum digital sum

def sum_of_digits(n):
    return sum(list(map(int, str(n).strip())))

maximum = 0
max_nums = []

for a in range(1,100):
    for b in range(1,100):
        num = a ** b
        num_digit = sum_of_digits(num)
        if num_digit > maximum:
            maximum = num_digit
            max_nums = [a, b]

print(max_nums, maximum)