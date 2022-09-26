# Find all Lychrel numbers below 10,000 (check out the problem definition for the weird definition)
# of a Lychrel number

# Done in a brute force way, could be done with caching/DP, but there isn't
# much room for speed up with only 10,000 numbers to check

def reverse_num(n):
    return int(str(n)[::-1])

lychrels = []

for n in range(1, 10001):
    num = n
    lychrel = True
    for _ in range(51):
        num = num + reverse_num(num)
        if num == reverse_num(num):
            # print(f"{n} is not a Lychrel, {num}")
            lychrel = False
            break
    if lychrel:
        # print(f"{n} is a Lychrel number")
        lychrels.append(n)
print(lychrels, len(lychrels))