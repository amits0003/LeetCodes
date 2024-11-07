"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing
consecutive identical characters (repeated 2 or more times) with the concatenation of the
character and the number marking the count of the characters (length of the run).
For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32",
replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.
Example 1:
Input: n = 4
Output: "1211"
Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:
"""
from pandas.core.window.doc import template_returns


class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"
        for _ in range(1,n):
            next_term = ""
            i = 0
            while i < len(term):
                count = 1
                while i+1 < len(term) and term[i] == term[i+1]:
                    i +=1
                    count +=1
                next_term +=  str(count) +term[i]
                i+= 1
            term = next_term

        return term

obj = Solution()
print(obj.countAndSay(4))

# using recursion

def countandSay(n):
    if n == 1:
        return "1"

    prev_term = countandSay(n-1)
    result = ""
    i = 0

    while i < len(prev_term):
        count = 1

        while i+1 <len(prev_term) and prev_term[i] == prev_term[i+1]:
            i+= 1
            count +=1

        result += str(count) + prev_term[i]
        i+=1

    return result