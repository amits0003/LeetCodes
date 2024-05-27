"""
The terms "brute force" and "exhaustive search" are often used interchangeably.
However, an exhaustive search generally refers to systematically trying all possible combinations of a solution space.

Let's consider an example of generating all possible 3-digit combinations using digits 0-9:
"""


def exhaustive_search():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                combination = f'{i}{j}{k}'
                print(combination)


# Example usage:
exhaustive_search()
