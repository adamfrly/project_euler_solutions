import math

def p(n):
    return n * (3 * n - 1 ) / 2

def is_pentagonal(n):
    # Identity from wikipedia
    num = (math.sqrt(24 * n + 1) + 1) / 6
    return num == int(num)

not_found = True
i = 0

while not_found:
    i = i + 1
    n = p(i)
    for j in range(i, 0, -1):
        m = p(j)
        if is_pentagonal(n - m) and is_pentagonal(n + m):
            result = n - m
            not_found = False
        
print(result)