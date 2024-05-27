"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

"""


def sqrt_integer(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number")

    if x == 0 or x == 1:
        return x

    start = 0
    end = x
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result

# Example usage
number = 16
print(f"The square root of {number} is {sqrt_integer(number)}")
