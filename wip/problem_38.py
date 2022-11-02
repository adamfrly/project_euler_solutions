import itertools
perms_str = list(itertools.permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"]))

perms = [int("".join(s)) for s in perms_str]

print(len(perms)) 