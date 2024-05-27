"""
Longest Substring Without Repeating Characters
"""

givenString = "abcabcbb"

"abc"
"bca"
"cab"
"bc"

"""
length for the longest substring is 3
{index : value }
substr = {i = 0, 1, ,2  : 
"""


def longestSubString1(strArr):
    substr = {}
    start = 0
    max_len = 0
    for i in range(len(strArr)):
        if strArr[i] in substr:
            start = max(start, substr[strArr[i]] + 1)
        substr[strArr[i]] = i
        max_len = max(max_len, i - start + 1)

    print(max_len)


longestSubString1(givenString)
