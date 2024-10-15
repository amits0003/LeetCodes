"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, v in enumerate(nums):
            if v != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

        # for i in range(k,len(nums)):
        #     nums[i] = 0

        return nums


nums = [0,1,0]
obj1 = Solution()
print(obj1.moveZeroes(nums))
