"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        if not nums:
            return [-1, -1]

        if nums:
            if target not in nums:
                return [-1, -1]

            if target in nums:
                for index, value in enumerate(nums):
                    if target == value:
                        res.append(index)
                        break

                i = len(nums) - 1
                while i >= 0:
                    if nums[i] == target:
                        res.append(i)
                        i -= 1
                        break

                if len(res) == 2:
                    return res
                else:
                    return [res[0], res[0]]


num = [1]
t = 1
obj1 = Solution()
print(obj1.searchRange(num, t))


# Method 2 :

class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        if not nums:
            return [-1, -1]

        if nums:
            if target not in nums:
                return [-1, -1]

        firsIndex = nums.index(target)
        lastIndex = len(nums) - 1 - num[::-1].index(target)

        res.append(firsIndex)
        res.append(lastIndex)

        # if len(res) == 2:
        #     return res
        # else:
        #     return [res[0], res[0]]
