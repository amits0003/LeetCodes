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


# strs = ["baab", "bacb", "b", "cbc"]
# strs1 = ["abab", "aba", ""]
# str2 = ["aac", "cab", "abb"]
# str3 = ["abca", "aba", "aaab"]
# print(longestCommonPrefix(str3))
# print(strs[1:])

def alternate_min_max(array):
    # Sort the array
    sorted_array = sorted(array)

    # Initialize result array
    result = []

    # Indices for filling result
    left, right = 0, len(array) - 1

    # Fill result with alternate min and max values
    for i in range(len(array)):
        if i % 2 == 0:
            result.append(sorted_array[right])
            right -= 1
        else:
            result.append(sorted_array[left])
            left += 1

    return result


# Example usage:
# array = [1, 23, 43, 5435, 6565, 69494, 242, 33]
# result = alternate_min_max(array)
# print("Array sorted in alternating min/max pattern:")
# print(result)


strs1 = ["flower", "flow", "flight"]
strs1 = sorted(strs1)
print(strs1)


def sol1(strs):
    ans = ""
    strs = sorted(strs)

    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans


print(sol1(strs1))
strs = ["baab", "bacb", "b", "bc"]
strs1 = ["abab", "aba", ""]
str2 = ["aac", "cab", "abb"]
str3 = ["abca", "aba", "aaab"]

print(sol1(strs))
print(sol1(strs1))
print(sol1(str2))
print(sol1(str3))


def sol2(str1):
    first = str1[0]
    last = str1[-1]
    ans = ""
    str1 = sorted(str1)

    for var in range(min(len(first), len(last))):
        if first[var] != last[var]:
            return ans
        ans += first[var]
    return ans


strs = ["flower", "flow", "flight"]
print(sol2(strs))
