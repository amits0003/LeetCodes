"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42
Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:
Input: s = " -042"
Output: -42
Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:
Input: s = "1337c0d3"
Output: 1337
Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:
Input: s = "0-1"
Output: 0
Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5
Input: s = "words and 987"
Output:
Explanation:
Reading stops at the first non-digit character 'w'.
"""


def ConvertStringToInt(s: str):
    s = s.strip()

    # print(s[0])
    if s[0] == "-" or s[0] == "+":
        res = ""
        for ele in s[1:]:
            try:
                ele1 = int(ele)
                res += str(ele1)
            except Exception as e:
                print(e)
                break
        newRes = s[0] + res
        return int(newRes)
    else:
        res = ""
        f = False

        for ele in s[0:]:
            try:
                ele1 = int(ele)
                res += str(ele1)
                # res = int(res)
                f = True
            except :
                f = False
                break

        if f:
            return int(res)
        return 0



# print(ConvertStringToInt(s1))

def ConvertStringToInt1(s):
    index = 0
    sign = 1
    s = s.strip()
    if not s :
        return 0
    sign, index = 1 if s[0] == "+" else -1, index+1
    # if s[0] in "-+":
    #     if s[0] == "+":
    #         sign = 1
    #         index += 1
    #     elif s[0] == "-":
    #         sign = -1
    #         index += 1

    result = 0
    while index < len(s) and s[index].isdigit():
        result = result*10 + int(s[index])
        index += 1

    result = result*sign

        # INT_MAX = 2 ** 31 - 1
        # INT_MIN = -2 ** 31
        #
        # if result < INT_MIN:
        #     return INT_MIN
        # if result > INT_MAX:
        #     return INT_MAX

    return result


s1 = "-042"
print(ConvertStringToInt1(s1))
