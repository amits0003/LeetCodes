"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

"""


def combinations(candidates, target):
    allCombinationList = []
    for ele in candidates:
        if ele == target:
            allCombinationList.append([target])
        elif target > ele:
            if (target - ele) in candidates:
                tempList = [ele, target - ele]
            else:
                tmpList1 = []
                tmpVar = target - ele
                while tmpVar > 0:
                    tmpVar = tmpVar - ele
                    if tmpVar in candidates:
                        tmpList1.append(tmpVar)
                allCombinationList.append([tmpList1])

    return allCombinationList


# There are two possibities of making a combination, i.e., to take an element or to not take an element.


def combinationSum(candidates, target):
    final = []

    def get_combinations(ind, target, arr, result):
        if ind == len(arr):
            if target == 0:
                final.append(result[:])
            return
        if arr[ind] <= target:
            result.append(arr[ind])
            get_combinations(ind, target - arr[ind], arr, result)  # to take the element
            result.pop()
        get_combinations(ind + 1, target, arr, result)  # to not take the element

    get_combinations(0, target, candidates, [])
    return final


candidates = [2, 3, 6, 7]
target = 7

print(combinationSum(candidates, target))
