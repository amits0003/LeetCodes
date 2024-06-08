"""
Write a function to find the longest common prefix string amongst an array of strings.
      If there is no common prefix, return an empty string "".
      Input: strs = ["flower","flow","flight"]
"""



tmp = "flow"


def longestCommonPrefix(strs):
    tmpPrefix = ""
    flag = True
    len2 = len(strs[1])
    len1 = len(strs[0])
    for index in range(len2 if len1 > len2 else len1):
        if strs[len(strs)-1] != "" and strs[0][0] == strs[len(strs)-1][0] and strs[0][0] == strs[1][0]:
            if strs[0][index] == strs[1][index]:
                tmpPrefix += strs[0][index]

    tempVar = ""

    for idx, val in enumerate(strs):
        if tmpPrefix in val[:len(tmpPrefix)]:
            flag = True
            continue
        else:
            idx1 = len(tmpPrefix)
            flag = False
            while idx1 > 0:
                if val == "":
                    return ""
                else:
                    tempVar = tmpPrefix[:idx1]
                    if tempVar in val[:len(tmpPrefix)]:
                        break
                idx1 = idx1 - 1

    if tempVar == tmpPrefix:
        return ""

    if flag :
        return tmpPrefix
    else :
        return tempVar



strs = ["flower", "flow", "floght"]
st1 = ['abc', 'bcd']
print(longestCommonPrefix(strs))
