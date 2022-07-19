# Find the product of the pythagorean triplet where a + b + c = 1000


# Brute force, took too long
# def is_triplet(a, b, c):
#     return a ** 2 + b ** 2 == c ** 2
#
# for a in range(1000):
#     for b in range(a, 1000):
#         for c in range(b, 1000):
#             print(c)
#             if is_triplet(a, b, c) and (a + b + c) == 1000:
#                 result = a * b * c

# print(result)

# Look at using Euclid's formula to generate pythagorean triples

for n in range(1000):
    for m in range(n, 1000):
        a = m ** 2 - n **2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if a + b + c == 1000:
            result = a * b * c
            triple_1 = a
            triple_2 = b
            triple_3 = c
            

print(f"{triple_1}, {triple_2}, {triple_3} are the numbers. Their product is {result}")