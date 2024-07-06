"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
"""


def MaximalRectangle(r,c):
    n = 5
    matrix = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]

    for row in matrix:
        print(row)