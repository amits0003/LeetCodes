"""
Brute force and exhaustive search are techniques used in computer science and programming
to solve problems by systematically trying all possible solutions.
These methods are often simple but may be inefficient for large problem instances.
"""


def brute_force_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found


# Example usage:
numbers = [2, 5, 8, 10, 13, 17, 21]
target_number = 13

result = brute_force_search(numbers, target_number)

if result != -1:
    print(f'Target {target_number} found at index {result}.')
else:
    print(f'Target {target_number} not found in the list.')
