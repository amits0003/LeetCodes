def find_closest_numbers(nums):
    # Sort the list in ascending order
    nums.sort()

    min_diff = float('inf')  # Initialize minimum difference to positive infinity
    closest_pair = None  # Initialize the pair of closest numbers

    # Iterate through the sorted list to find the minimum difference
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (nums[i], nums[i + 1])

    return closest_pair


# Example usage:
nums = [1, 44, 4, 5, 6, 90,  34, 56, 12, 54, 67, 3]
closest_numbers = find_closest_numbers(nums)
print("Two closest numbers:", closest_numbers)
