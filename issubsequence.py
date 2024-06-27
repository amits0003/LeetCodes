"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""
from operator import mod


def isSubSequence(a,b):
    m,n = len(a), len(b)
    i,j = 0, 0
    newArr = []

    while i < m and j < n:
        if a[i] == b[j]:
            i = i + 1
            newArr.append(b[j])
        j = j + 1

    #print(newArr)
    return i == len(a)


d = 'acc'
f = "abcde"
print(f[:])
print(isSubSequence(d,f))
#
#
# def sq():
#     flag = False
#     for i, v in enumerate(f):
#         for x, y in enumerate(d):
#             if y in f:
#                 if i<=x:
#                     flag = True
#                 else:
#                     flag = False
#     return flag


# print(sq())
#
#
# def reverse_number(num):
#     # Convert number to string (handle negative sign if present)
#     num_str = str(num)
#
#     # Check if number is negative
#     is_negative = num_str[0] == '-'
#
#     # Reverse the string (excluding the negative sign if present)
#     reversed_str = num_str[:0:-1] if is_negative else num_str[::-1]
#
#     # Convert the reversed string back to an integer
#     reversed_num = int(reversed_str)
#
#     # Add back the negative sign if the original number was negative
#     return -reversed_num if is_negative else reversed_num

#
# def reverse_number(n):
#     reversed_n = 0
#     n = mod(n)
#
#     while n != 0:
#         last_digit = n % 10  # Extract the last digit of n
#         reversed_n = reversed_n * 10 + last_digit  # Append the last digit to reversed_n
#         n = n // 10  # Remove the last digit from n
#
#     return reversed_n
#
#
# # Test cases
# print(reverse_number(123))  # Output: 321
# print(reverse_number(-456))  # Output: -654
# print(reverse_number(120))
#
# # Test cases
# print(reverse_number(123))  # Output: 321
# print(reverse_number(-456))  # Output: -654
# print(reverse_number(120))


