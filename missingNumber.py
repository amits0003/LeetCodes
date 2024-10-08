"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""
from typing import List


# method 1 : looping
def missingNumber(nums):
    len_nums = len(nums)

    for i in range(0, len_nums + 1):
        if i not in nums:
            return i


nums = [0, 1]
print(missingNumber(nums))


# Method 2 : using Sum Approach : Optimized Way

def missingNumber1(nums):
    len_nums = len(nums)

    total_sum = len_nums * (len_nums + 1) // 2
    arr_sum = sum(nums)

    return total_sum - arr_sum


nums = [0, 1]
print(missingNumber1(nums))

# Method 3: using Bitwise Operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)  # Start with n since we're XORing 0 to n

        # XOR all indices and values
        for i in range(len(nums)):
            missing ^= i ^ nums[i]

        return missing
