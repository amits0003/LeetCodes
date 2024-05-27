"""
Given a set of coin denominations and a target amount,
find the number of ways to make the target amount using any combination of coins.
"""

def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# Example usage:
coins = [1, 2, 5]
amount = 5

print("Ways to make change:", coin_change_ways(coins, amount))
