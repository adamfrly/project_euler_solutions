# Find the longest Collatz sequence under 1 million
# First time using dynamic programming (memoization) and recursion


def collatz_seq(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz_seq(n // 2) + 1
    else:
        return collatz_seq(3 * n + 1) + 1

memo = {}
def collatz_seq_memo(n):
    if not n in memo:
        if n == 1:
            memo[n] = 1
        elif n % 2 == 0:
            memo[n] = collatz_seq(n // 2) + 1
        else:
            memo[n] = collatz_seq(3 * n + 1) + 1
    return memo[n]

max = 0
result = 1
for i in range(1, 1000001):
    trial = collatz_seq_memo(i)
    if trial > max:
        max = trial
        result = i

print(result)

