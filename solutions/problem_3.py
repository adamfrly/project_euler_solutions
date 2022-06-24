# Print the largest prime factor of 60085145143

number = 600851475143

def prime_factorization(num):
    prime_factors = []
    d = 2
    while d * d < num:
        while num % d == 0:
            prime_factors.append(d)
            num = num / d
        d = d + 1

    if num > 1:
        prime_factors.append(num)

    return prime_factors

print(max(prime_factorization(number)))