"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character,
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

"""


# without dp

def checkRegexPattern(s, p):
    if s == p:
        return True

    if not p:
        return not s

    first_match = bool(s) and (p[0] == s[0] or p[0] == ".")

    if len(p) >= 2 and p[1] == "*":
        return checkRegexPattern(s, p[2:]) or (first_match and checkRegexPattern(s[1:], p))
    else:
        return first_match and checkRegexPattern(s[1:], p[1:])


s1 = "aa"
p1 = "a"

print(checkRegexPattern(s1, p1))


# with dp

def isMatch(s, p):
    n = len(s)
    m = len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0]= True

    for j in range(1, m+1):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-2]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if p[j-1] == s[i-1] or p[j-1] == ".":
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i][j-2]

                if p[j-2] == s[i-1] or p[j-2] == ".":
                    dp[i][j] |= dp[i-1][j]

    return dp[n][m]


print(isMatch(s1, p1))
