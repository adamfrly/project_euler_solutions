# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2


def decimalToBinary(n):
    # converting decimal to binary
    # and removing the prefix(0b)
    return bin(n).replace("0b", "")

sum = 0

for n in range(1,1000001):
    n_2 = decimalToBinary(n)
    n_str = str(n)

    if n_str == n_str[::-1] and n_2 == n_2[::-1]:
        sum += n

print(sum)