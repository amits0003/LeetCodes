"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed)
parentheses substring.
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0

"""


def longestValidParenthesis(s):
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length



s = ")()())"
print(longestValidParenthesis(s))

# while i != lenStr:
#     if s[0] in bracketMap:
#         print(s[i])
#         if s[i + 1] in bracketMap.values():
#             validStr.append(s[i])
#             validStr.append(s[i + 1])
#             s = s[i + 1:]
#     else:
#         s = s[i + 1:]
#     i = i + 1
