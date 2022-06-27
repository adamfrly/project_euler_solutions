from math import comb

def num_grid_paths(n):
    return comb(2*n, n)

print(num_grid_paths(20))