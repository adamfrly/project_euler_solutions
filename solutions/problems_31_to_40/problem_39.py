# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}.
# For which value of p ≤ 1000, is the number of solutions maximised?

# This solution gives the right answer, but that's kind of a fluke. Setting k, n, and m to 500 is arbitrary and there was no guarantee 
# that they would produce all pythagorean triples with sum less than 1000

p_counts = {}
tris = []

for k in range(1, 500):
    for m in range(1, 500):
        for n in range(1, 500):
            a = k * (m ** 2 - n ** 2)
            b = k * 2 * m * n
            c = k * (m **2 + n ** 2)
            p = a + b + c
            tri = [a, b, c]
            tri.sort()

            if p > 1000 or a <= 0 or b <= 0 or c <= 0:
                break
            if tri in tris:
                break
            else:
                tris.append(tri)
            if p in p_counts:
                p_counts[p] = p_counts[p] + 1
            else:
                p_counts[p] = 1

print(max(p_counts, key=p_counts.get))
