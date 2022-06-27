# Find the first triangle number to have more than 500 divisors

divs = []

def divisors(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            result.append(n//i)
    return result

num = 0
triangle = 0
while len(divs) < 500:
    num = num + 1
    triangle = triangle + num
    divs = divisors(triangle)

print(triangle)