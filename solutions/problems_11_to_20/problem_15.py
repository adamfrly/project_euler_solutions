# Find the total number of possible routes on a 20 by 20 grid where you can only move right or down

from math import comb

def num_grid_paths(n):
    return comb(2*n, n)

print(num_grid_paths(20))