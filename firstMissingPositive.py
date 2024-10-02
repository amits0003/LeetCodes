def firstMissingPositive(nums):
    n = len(nums)

    # Place each number in its correct position (if possible)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] to its correct position nums[nums[i] - 1]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find the smallest positive integer missing
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all numbers from 1 to n are present, the result is n + 1
    return n + 1


nums = [1,2,0]


# print(firstMissingPositive(nums))
def firstMissingPositive1(nums):
    nums.sort(reverse=False)
    n = len(nums)
    for i in range(n):
        if nums[i] != i+1:
            return i+1


print(firstMissingPositive1(nums))
