"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of
the integer. The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""


def plusOne(digits):
    resStr1 = ""
    for ele in digits:
        resStr1 = resStr1 + str(ele)

    resInt = int(resStr1)
    incResInt = resInt + 1

    nStr = str(incResInt)
    newL = []
    for ele in nStr:
        newL.append(int(ele))

    return newL


# digits = [1, 2, 3]
# print(plusOne(digits))


def plusOne2(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        else:
            digits[i] = 0
    return [1] + digits


digits = [4, 3, 9, 9]
print(plusOne2(digits))