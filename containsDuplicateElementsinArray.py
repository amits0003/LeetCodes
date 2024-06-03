"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

"""
from itertools import count


def containsDuplicate1(nums):
    for i, v in enumerate(nums):
        if nums[i] in nums[i + 1:]:
            return True
    return False


def containsDuplicate2(nums):
    newList = set()
    flag = False
    for ele in nums:
        if ele in newList:
            flag = True
        newList.add(ele)
    return flag


def containsDuplicates3(nums):
    nums.sort()

    for ele in range(1, len(nums)):
        if nums[ele] == nums[ele -1]:
            return True
    return False


nums = [1, 2, 3, 4]
print(containsDuplicates3(nums))
