# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital

results = []

# There are only two cases when a multiplicand/multiplier/product identity can yeild 9 digits
# A 2 digit number times a 3 digit number
# A 1 digit number times a 4 digit number

for n in range(10, 100):
    for m in range(100, 1000):
        prod = n * m
        n_str = str(n)
        m_str = str(m)
        prod_str = str(prod)
        if "".join(sorted(n_str + m_str + prod_str)) == "123456789" and prod not in results:
            results.append(prod)

for n in range(1, 10):
    for m in range(1000, 10000):
        prod = n * m
        n_str = str(n)
        m_str = str(m)
        prod_str = str(prod)
        if "".join(sorted(n_str + m_str + prod_str)) == "123456789" and prod not in results:
            results.append(prod)

print(results, sum(results))
