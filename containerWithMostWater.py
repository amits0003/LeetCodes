"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Solutions :
Two end points of 2nd element of array = [1,0] and [1,8]
Two End points of the last element of array = [8,0] and [8,7]

Calculating Area :
Difference in X axis between two max possible vertical lines = [8,0] - [1,0] = 7
common height from two max possible vertical lines [1,8] and [8,7] are 7

So max Area = 7 * 7 = 49

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        # print(len(height))

        while left < right :
            max_area = max(max_area, min(height[left], height[right]) * (right-left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


obj1 = Solution()
a = [1,8,6,2,5,4,8,3,7]
print(obj1.maxArea(a))
