# Find the last ten digits of 28433×2^7830457+1

num = str(28433 * 2 ** 7830457 + 1)
num_10 = num[-10:]
print(len(num), num_10)

