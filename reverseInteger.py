"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)

        rev_x = 0

        while x != 0:
            reminder = x%10
            rev_x = rev_x*10 + reminder
            x = x//10

        if rev_x > 2147483647 or rev_x < -2147483648:
            return -10
        else:
            return rev_x * sign





dig = 234
div = 0
while dig != 0:
    rm = dig % 10
    print(rm)

    div = div*10 + rm
    dig = dig //10

print(div)
