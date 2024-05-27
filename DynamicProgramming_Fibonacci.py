"""
The Fibonacci sequence is a
classic example of dynamic programming where you can optimize recursive calculations by storing and reusing intermediate results.
"""


# Recursive approach (inefficient)

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Dynamic Programming approach (efficient)
def fibonacci_dynamic(n):
    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# Example usage:
# print("Fibonacci (Recursive):", fibonacci_recursive(99))
print("Fibonacci (Dynamic Programming):", fibonacci_dynamic(9999995))
