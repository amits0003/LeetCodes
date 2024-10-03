"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

"""
t = "ccd"


def findPalindromeSubstring(str1):
    n = len(str1)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    start = 0
    max_length = 1
    for i in range(n-1):
        if str1[i] == str1[i+1]:
            dp[i][i+1] = True
            start =  i
            max_length = 2

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if str1[i] == str1[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_length = length

    return str1[start: start+max_length]


print(findPalindromeSubstring(t))


def palindromeSubstring(s):
    for i, v in enumerate(s):
        if s[i] == s[len(s) - i-1]:
            tempS3 = s[i:len(s) - i]
            tempS4 = tempS3[::-1]
            if tempS4 == tempS3:
                return tempS3
        else:
            tempS1 = s[i + 1:]
            temps2 = s[::-1]
            if tempS1 == temps2:
                return tempS1


# print(palindromeSubstring(s))


