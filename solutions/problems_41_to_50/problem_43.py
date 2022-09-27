# Find the sum of all pandigital 0-9 numbers with a weird prime number divisiblity property

# Done with brute force

import itertools

perms_tuples = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

perms = [''.join(map(str, tple)) for tple in perms_tuples]

# print(perms[7], type(perms[7]))

result = []

for perm in perms:
    good = True
    if int(perm[1:4]) % 2 != 0:
        good = False
    if int(perm[2:5]) % 3 != 0:
        good = False
    if int(perm[3:6]) % 5 != 0:
        good = False
    if int(perm[4:7]) % 7 != 0:
        good = False
    if int(perm[5:8]) % 11 != 0:
        good = False
    if int(perm[6:9]) % 13 != 0:
        good = False
    if int(perm[7:10]) % 17 != 0:
        good = False
    if good:
        result.append(int(perm))

print(result, sum(result))