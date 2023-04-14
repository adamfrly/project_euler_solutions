def get_fract_const(i):
    if i % 3 == 1:
        return 2 * (i + 2)  // 3
    return 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

nums = [2,3]
LIMIT = 100
for k in range(2, LIMIT):
    fract_const = get_fract_const(k-1)
    new_num = nums[-1] * fract_const + nums[-2]
    nums.append(new_num)

print(nums[-1], sum_digits(nums[-1]))
