# Number of distinct answers to a^b, a in [2, 100], b in [2,100]

allCombinations = []
for a in range(2, 101):
    for b in range(2, 101):
        allCombinations.append(a ** b)

uniqueCombinations = list(set(allCombinations))
uniqueCombinations.sort()
print(len(uniqueCombinations))