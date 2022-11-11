# Find the four cases where you can naively "cross cancel" digits in a 2 digit by 2 digit fraction to get the right answer

candidates = []

for i in range(1, 10):
    for j in range(1, 10):
        for n in range(1, 10):
            for m in range(1, 10):
                num = float(str(i) + str(j)) / float(str(n) + str(m))
                if num < 1:
                    if num == float(i) / float(n) and i == m:
                        candidates.append(f"{i}{j}/{n}{m}")
                    if num == float(i) / float(m) and j == n:
                        candidates.append(f"{i}{j}/{n}{m}")
                    if num == float(j) / float(n) and i == m:
                        candidates.append(f"{i}{j}/{n}{m}")
                    if num == float(j) / float(m) and i == n:
                        candidates.append(f"{i}{j}/{n}{m}")

cands = list(set(candidates)) # There are more numbers in here than there should be, need to figure out why

print(cands) # Cands from this are actually 26/65, 49/98, 19/95, 16/64

print(26/65 * 49/98 * 19/95 * 16/64) # Equals 1/100