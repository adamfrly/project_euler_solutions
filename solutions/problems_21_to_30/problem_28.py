
# Attempt at creating a polynomial based on the first 4 rings, was done late so I failed miserably
# def solution(x):
#     return 16/3 * x **3 + 10 * x ** 2 + 26 / 3 * x + 1

# print(solution(1001))

# Brute force method
size = 1001
result = 1
n = 1
for i in range(2, size, 2):
    for j in range(4):
        n += i
        result += n
print(result)