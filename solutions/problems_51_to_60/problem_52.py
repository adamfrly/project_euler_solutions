# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

not_found = True
num = 1
while not_found:
    num1 = list(str(num))
    num1.sort()
    num2 = list(str(2 * num))
    num2.sort()
    num3 = list(str(3 * num))
    num3.sort()
    num4 = list(str(4 * num))
    num4.sort()
    num5 = list(str(5 * num))
    num5.sort()
    num6 = list(str(6 * num))
    num6.sort()
    if num1 == num2 and num2 == num3 and num3 == num4 and num4 == num5 and num5 == num6:
        print(num)
        not_found = False
    num = num + 1

