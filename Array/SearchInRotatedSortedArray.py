"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""
from typing import List


def SearchInRotatedSortedArray(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        mid_ele = nums[mid]

        if mid_ele == target:
            return mid

        if nums[low] <= mid_ele :
            if nums[low] <= target < nums[mid] :
                high = mid -1
            else:
                low = mid +1
        else:
            if nums[low] < target <= nums[high]:
                low = mid+1
            else:
                high = mid - 1

    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(SearchInRotatedSortedArray(nums, target))


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1
