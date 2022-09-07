# Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
from itertools import permutations


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = list(permutations(digits)) # This already outputs things in lexicographocal order, so kind of a cheat


millionth = perms[999999]
millionth_str = ""
for thing in millionth:
    millionth_str = millionth_str + str(thing)


print(millionth_str)