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

# Method 1 : using dynamic programming

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

# Method 2 : using for loop

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


# Method 3 : using expand around center approach

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the length of the palindrome
    return right - left - 1


def longest_palindrome_substring(s):
    if not s:
        return ""

    start, end = 0, 0  # Pointers to keep track of the longest palindrome

    for i in range(len(s)):
        # Case 1: Odd length palindrome (single center)
        len1 = expand_around_center(s, i, i)
        # Case 2: Even length palindrome (two centers)
        len2 = expand_around_center(s, i, i + 1)

        # Find the maximum length between the two cases
        max_len = max(len1, len2)

        # Update start and end pointers if a longer palindrome is found
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    # Return the longest palindrome substring
    return s[start:end + 1]


# Example usage:
input_str = "babad"
print(longest_palindrome_substring(input_str))




