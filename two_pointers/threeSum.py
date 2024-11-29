"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

"""
from ctypes.wintypes import SIZEL
from logging import currentframe
from typing import List


class Solution:
    def sumThreeNum(self, nums:List[int], target:int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n-2):
            left, right = i+1, n-1

            while left < right :
                current_sum  = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target :
                    left +=1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum

nums = [-1, 2, 1, -4]
target = 1
obj = Solution()
print(obj.sumThreeNum(nums, target))
