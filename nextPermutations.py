"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1],
 [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical
order, then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order
(i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

from itertools import permutations, combinations


# Method 1 : Not efficient for larger Size arrays

def nextPermutation(nums):
    res = permutations(nums)

    coll1 = []

    for ele in res:
        coll1.append(list(ele))

    coll1.sort()
    print(coll1[-1])
    finalItem = []
    for i, v in enumerate(coll1):
        if v == nums:
            if v == coll1[-1]:
                finalItem.append(coll1[0])
            else:
                finalItem.append(coll1[i + 1])
    nums = finalItem[0]
    return nums


arr1 = [1, 2, 3]
print(nextPermutation(arr1))


def nextPermutationThroughLexicoGraphicalOrder(nums):
    i = len(nums) - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # if "i" is found at the location

    if i >= 0:
        j = len(nums) - 1

        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    # reverse the subarray nums[i+1:] to get the next lexicographical permutation

    nums[i + 1:] = reversed(nums[i + 1:])

    return nums


arr1 = [1, 2, 3]
print(nextPermutationThroughLexicoGraphicalOrder(arr1))
