"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false

"""


def isHappy(n):
    if n == 1:
        return True

    if n <= 0:
        return False

    while n != 1:
        res = 0
        n = str(n)
        for i, v in enumerate(n):
            v = int(v)
            res = res + (v * v)
        if res == 7:
            return True
        if res in range(2, 10):
            return False
        elif res == 1:
            return True

        n = res


d = 1111111
print(isHappy(d))
