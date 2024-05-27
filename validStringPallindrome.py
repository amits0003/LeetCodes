"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
 non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
 numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

def validStringPalindrome(s):
    if s == "" or s == " ":
        return True

    newList = ""
    for ele in s:
        if ele.isalnum():
            newList+=ele

    n = newList.lower()
    m = newList[::-1].lower()

    return True if n ==m else False

s = "race a car"

print(validStringPalindrome(s))