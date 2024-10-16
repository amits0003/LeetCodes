"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
 [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and
 if the quotient is strictly less than -231, then return -231.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define constants for 32-bit signed integer limits
        MAX_INT = 2 ** 31 - 1  # 2147483647
        MIN_INT = -2 ** 31  # -2147483648

        # Handle edge case for overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values for ease
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize quotient
        quotient = 0

        # Use bitwise shifting to subtract the largest multiples of the divisor
        while dividend >= divisor:
            # Initialize temp as divisor and the multiple count as 1
            temp, multiple = divisor, 1

            # Find the largest double of divisor that is less than or equal to dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Subtract that large multiple from the dividend
            dividend -= temp
            quotient += multiple

        # Apply the sign to the quotient
        quotient = -quotient if negative else quotient

        # Clamp the result within the 32-bit signed integer range
        return max(MIN_INT, min(MAX_INT, quotient))