"""
Given two strings s1 and s2 consisting of
lowercase characters, the task is to check whether the two given strings are
anagrams of each other or not. An anagram of a string is another string that contains the same characters,
only the order of characters can be different. For example, “act” and “tac” are anagrams of each other.

Input: str1 = “listen”  str2 = “silent”
Output: “Anagram”
Explanation: All characters of “listen” and “silent” are the same.
Input: str1 = “gram”  str2 = “arm”
Output: “Not Anagram”
"""

print("Hello World")

s1 = "gram"
s2 = "arm"


def create_dict(l1):
    dict_str1 = {}
    for ele in l1:
        if ele in dict_str1:
            # flag = True
            dict_str1[ele] += 1
        else:
            dict_str1[ele] = 1
    return dict_str1


def check_anagram(s1, s2):
    l1 = [e for e in s1]
    l2 = [b for b in s2]

    print(l1)
    print(l2)

    dict_str1 = create_dict(l1)
    dict_str2 = create_dict(l2)
    print(dict_str1)
    print(dict_str2)

    return dict_str1 == dict_str2


print(check_anagram(s1, s2))