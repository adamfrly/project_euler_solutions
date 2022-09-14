# Find the next triangle number that is also pentagonal and hexagonal after 40755

# I chose to look at the first 100000 numbers arbitratily and so this is really just a brute force soltuion, it could be optimized greatly

def first_n_tri_num(n):
    return [int(0.5*i*(i + 1)) for i in range(1, n + 1)]

def first_n_pent_num(n):
    return [int(0.5*i*(3 * i - 1)) for i in range(1, n + 1)]

def first_n_hex_num(n):
    return [int(i*(2 * i - 1)) for i in range(1, n + 1)]

tri = first_n_tri_num(100000)
pent = first_n_pent_num(100000)
hex = first_n_hex_num(100000)

candidates = []
for num in tri:
    if num in pent and num in hex:
        candidates.append(num)

print(candidates)