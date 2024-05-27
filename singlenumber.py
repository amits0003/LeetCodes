"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


def singleNum(nums):
    for ele in nums:
        if nums.count(ele) == 1:
            return ele


nums = [2, 2, 1]

d = singleNum(nums)

print(d)

# Define lambda expression
find_unique = lambda nums: next(filter(lambda ele: nums.count(ele) == 1, nums))

# Example usage:
nums = [1, 2, 3, 2, 4, 3, 5]
result = find_unique(nums)
print(result)  # This will print the unique element


def singleNums(nums):
    return lambda ele: nums.count(ele) == 1

# Example usage:
nums = [1, 2, 3, 2, 4, 3, 5]

# Define a function to check if an element is unique
is_unique = singleNums(nums)

# Filter the list to find the unique element
unique_elements = filter(is_unique, nums)

# Get the first unique element
result = next(unique_elements, None)

print(result)  # This will print the first unique element in the list
