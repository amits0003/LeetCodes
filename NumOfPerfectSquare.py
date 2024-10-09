"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with
itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


def PerfectSquareNumber(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return i
        i += 1
    return None


def NumOfPerfectSquare(n):
    if n == 0:
        return []

    i = 1

    minSol = None
    while i * i <= n:
        temp = n - (i * i)
        tempSol = NumOfPerfectSquare(temp)
        curr_sol = [i * i] + tempSol

        if minSol is None or len(curr_sol) < len(minSol):
            minSol = curr_sol

        i += 1
    return minSol


print(NumOfPerfectSquare(12))


# Method 2 using DP :

def NumOfPerfectSquare(n):
    # Create a DP array to store the minimum number of perfect squares that sum up to i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 perfect squares sum up to 0

    # List of perfect squares up to n
    perfect_squares = []

    i = 1
    while i * i <= n:  # Instead of using math.sqrt(), generate perfect squares manually
        perfect_squares.append(i * i)
        i += 1

    # Fill the dp array manually
    for i in range(1, n + 1):
        for square in perfect_squares:
            if i >= square:
                # Manually compute the minimum between dp[i] and dp[i - square] + 1
                if dp[i - square] + 1 < dp[i]:
                    dp[i] = dp[i - square] + 1

    return dp[n]
