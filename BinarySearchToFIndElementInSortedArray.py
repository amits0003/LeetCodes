"""
Scenario 1: Binary Search
Binary search is a classic example of a divide and conquer algorithm.
The problem is to find a specific element in a sorted array.

"""


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Element found
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found


# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5

result = binary_search(sorted_array, target_element)

if result != -1:
    print(f'Target {target_element} found at index {result}.')
else:
    print(f'Target {target_element} not found in the array.')
