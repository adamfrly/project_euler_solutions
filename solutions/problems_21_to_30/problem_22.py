# Sort the names in names.txt, then multiply them by their index in the list (starting at 1)

import numpy as np

names = np.loadtxt("solutions\problems_21_to_30\\names.txt", dtype=str, delimiter=",")

def name_value(name):
    total = 0
    for letter in name:
        total = total + ord(letter) - 64
    return total

# Kind of a cheater way to do it, I think the intention is to make your own sorting algorithm based on looking at each letter in the name
names_sorted = np.sort(names)

list_of_name_vals = []
for i, name in enumerate(names_sorted):
    list_of_name_vals.append(name_value(name) * (i + 1))

result = sum(list_of_name_vals)

print(result)