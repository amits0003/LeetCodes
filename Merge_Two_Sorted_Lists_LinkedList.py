"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""

list1 = [1,2,4]
list2 = [1,3,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        list1.sort()
        list2.sort()

        newList = list1 + list2

        newList.sort()

        return newList


def mergeUsinglinkedListApproach(l1, l2):
    head = ListNode(0)
    current = head

    while l1 is not None or l2 is not None :
        if l1.val < l2.val :
            current.next = l1
            l1 = l1.next

        else :
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1 :
        current.next = l1
    if l2 :
        current.next = l2

    return head



obj1 = Solution()
print(obj1.mergeTwoLists(list1, list2))


