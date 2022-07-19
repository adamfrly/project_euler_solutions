# Implement the Ackermann function, and calculate A(n,n) from n=0 to 6

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n-1))

for n in range(1,7):
    result = ackermann(n,n)
    print(f"{n}: {result}")