"""
Given two strings s and t, return the number of distinct subsequences of
s which equals t.A subsequence of a string is a new string that is formed
from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters
Input: s = "babgbag", t = "bag"
"""

# without dynamic programming

def numDistinct(s, t):
    def count_subsequences(s, t, i, j, memo):
        # If we've matched the entire t string, return 1
        if j == len(t):
            return 1
        # If we've exhausted the s string, return 0
        if i == len(s):
            return 0
        # Check if result is already computed
        if (i, j) in memo:
            return memo[(i, j)]

        # Option 1: Skip the current character in s
        result = count_subsequences(s, t, i + 1, j, memo)

        # Option 2: Match the current character in s with the current character in t
        if s[i] == t[j]:
            result += count_subsequences(s, t, i + 1, j + 1, memo)

        # Memoize the result
        memo[(i, j)] = result
        return result

    return count_subsequences(s, t, 0, 0, {})
#
# # Example usage:
# s = "babgbag"
# t = "bag"
# print(numDistinct(s, t))  # Output: 5


# with ynamic programming

def numDistinct(s, t):
    m, n = len(s), len(t)

    # Create a 2D array with (m+1) x (n+1) dimensions
    dp = [[2] * (n + 1) for _ in range(m + 1)]
    print(dp)

    # Initialize the first column, as an empty string is a subsequence of any string
    for i in range(m + 1):
        dp[i][0] = 1

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]

# Example usage:
s = "babgbag"
t = "bag"
print(numDistinct(s, t))  # Output: 5

