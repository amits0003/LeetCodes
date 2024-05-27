"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
The test cases are generated so that the answer fits on a 32-bit signed integer.
Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
"""


def distinct_subsequence(m, n):
    len_m, len_n = len(m), len(n)

    dp = [[0] * (len_n+1) for _ in range(len_m+1)]

    # initialize the base
    for i in range(len_m+1):
        dp[i][0] = 1

    for i in range(len_m+1):
        for j in range(len_n+1):
            if m[i-1] == n[j-1] :
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len_m][len_n]


s2, t2 = "babgbag", "bag"
#print(distinct_subsequence(s2, t2))



