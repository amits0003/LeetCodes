"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.
"""


def longestCommonPrefix(strs):
    test_common_prefix = ""
    if len(strs) >= 2:
        len_idx1 = len(strs[0])
        len_idx2 = len(strs[1])

        for index in range(len_idx2 if len_idx1 > len_idx2 else len_idx1):
            # print(strs[0][index])
            if strs[len(strs) - 1] != "" and strs[0][0] == strs[len(strs) - 1][0] and strs[0][0] == strs[1][0]:
                if strs[0][index] == strs[1][index]:
                    test_common_prefix += strs[0][index]

        if test_common_prefix == "":
            return ""

        tempVar = ""
        flag = True
        for idx, val in enumerate(strs):
            # print(val)
            if test_common_prefix in val[:len(test_common_prefix)]:
                continue
            else:
                flag = False
                idx1 = len(test_common_prefix)
                while idx1 > 0:
                    if val == "":
                        return ""
                    else:
                        tempVar = test_common_prefix[:idx1]
                        if tempVar in val[:len(test_common_prefix)]:
                            break
                        idx1 = idx1 - 1

        if tempVar == test_common_prefix:
            return ""

        if flag:
            return test_common_prefix
        else:
            return tempVar

    else:
        if strs == [""]:
            return ""
        elif len(strs) == 1 and strs != [""]:
            return strs


strs = ["baab", "bacb", "b", "cbc"]
strs1 = ["abab", "aba", ""]
str2 = ["aac", "cab", "abb"]
str3 = ["abca", "aba", "aaab"]
# print(longestCommonPrefix(str3))
# print(strs[1:])

