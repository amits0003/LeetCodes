"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""

# Solution = Time Complexity & Space Complexity O(n)


def convert(s, n):
    rows = [''] * n
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char

        if current_row == 0 or current_row == n - 1:
            going_down = not going_down

        current_row += 1 if going_down else -1

    return "".join(rows)
