# Find how many ways 2 pounds can be made using any number of coins

def count_change(coins, n, sum):
    if (sum == 0):
        return 1
    if (sum < 0):
        return 0
    if (n <= 0):
        return 0
 
    return count_change(coins, n - 1, sum) + count_change(coins, n, sum-coins[n-1])

coin_purse = [1, 2, 5, 10, 20, 50, 100, 200]
n = len(coin_purse)
total = 200

print(count_change(coin_purse, n, total))