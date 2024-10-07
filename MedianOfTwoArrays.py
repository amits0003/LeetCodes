"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resultantArray = nums1 + nums2
        resultantArray.sort()

        len_arr = len(resultantArray)
        medianArr = 0
        # print(len_arr)
        med = len_arr // 2

        if len_arr % 2 == 0:
            # print(med-1, med)
            medianArr = (resultantArray[med] + resultantArray[med-1]) / 2
        elif len_arr % 2 != 0:
            medianArr = resultantArray[med]

        return medianArr


nums1 = [1, 2]
nums2 = [3,4,5]

obj1 = Solution()
print(obj1.findMedianSortedArrays(nums1, nums2))
