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
s = "ccd"


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


print(palindromeSubstring(s))
