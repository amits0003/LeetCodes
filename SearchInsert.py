"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""


def searchInsert(nums, target):
    pos = 0
    for i, v in enumerate(nums):
        if target in nums:
            l = len(nums)
            while l >0:
                if v == target:
                    pos = i
                l = l-1
        else:
            if target-v == 1:
                nums.insert(i+1, target)
                pos = i+1
            elif target-v > 1 and i == len(nums)-1:
                nums.append(target)
                pos = len(nums) - 1
                break
            elif target-v < 1 :
                nums.insert(i, target)
                pos = i
                break

    print(nums)
    return pos


nums = [3,6,7,8,10]
target = 5
print(searchInsert(nums, target))
