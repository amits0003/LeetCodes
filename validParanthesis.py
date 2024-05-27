def validParenthesis(s):
    bracketMap = {"(": ")",
                  "{": "}",
                  "[": "]"}
    stack = []

    for ele in s:
        if ele in bracketMap:
            stack.append(ele)
        elif ele in bracketMap.values():
            print(ele)
            if not stack:
                return False
            top = stack.pop()

            if bracketMap[top] != ele:
                return False

    return len(stack) == 0

s1 = "()"
print(validParenthesis(s1))  # Output: True

s2 = "()]{}"
print(validParenthesis(s2))  # Output: True