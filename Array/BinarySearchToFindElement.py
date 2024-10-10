"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
from typing import List


def binarySearchToFindElement(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (high + low) // 2

        mid_ele = nums[mid]

        if mid_ele == target:
            return mid
        elif mid_ele < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(binarySearchToFindElement(nums, target))

# Method 2
# for i in range(len(nums)):
#     if nums[i] == target:
#         return i
