"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:
Input: s = "abcde", goal = "abced"
Output: false
"""
s1 = "abcde"
goal1 = "cdeab"

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        m,n = len(s), len(goal)

        if m!=n:
            return False
        if m ==n:
            if goal in (s+s):
                return True
            else:
                return False






