# Find the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1
# Problem scope minimization due to analysis from https://www.mathblog.dk/project-euler-38-pandigital-multiplying-fixed-number/

result = 0
for i in range(9487, 9233, -1):
    result = int(str(i) + str(2*i))
    result_list = [int(x) for x in str(result)]
    result_list.sort()
    if result_list == [1,2,3,4,5,6,7,8,9]:
        break

print(result)