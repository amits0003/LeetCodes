"""
Suppose you want to make change for a given amount using the fewest number of coins.
You have a set of coin denominations, and you want to find the optimal combination.

"""


def min_coins(coins, target_amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    result = []
    remaining_amount = target_amount

    for coin in coins:
        while remaining_amount >= coin:
            result.append(coin)
            remaining_amount -= coin

    return result


# Example usage:
coin_denominations = [25, 10, 5, 1]
amount = 63

change = min_coins(coin_denominations, amount)
print("Minimum coins for change:", change)
