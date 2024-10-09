"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""
import heapq
from typing import Optional, List


# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Initialize the heap
        for l in lists:
            if l:
                # Push a tuple with (node value, node) to the heap
                heapq.heappush(min_heap, (l.val, l))

        root = ListNode()  # Dummy node
        current = root

        while min_heap:
            # Pop the smallest node from the heap
            smallest_value, smallest_node = heapq.heappop(min_heap)
            current.next = smallest_node
            current = current.next

            # If the smallest node has a next node, push it to the heap
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, smallest_node.next))

        return root.next


# Method 2 : with divide and conquer method

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    # Function to merge two sorted linked lists
    def merge_two_lists(self, l1, l2):
        # Create a dummy node to help build the result list
        dummy = ListNode()
        current = dummy

        # Compare the nodes of both lists and merge them
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append the remaining nodes, if any
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next
  
    # Helper function to recursively merge the lists
    def merge_lists_helper(self, lists, start, end):
        # Base case: if there's only one list
        if start == end:
            return lists[start]

        # Recursive case: divide the lists into two halves and merge them
        mid = (start + end) // 2
        left_merged = self.merge_lists_helper(lists, start, mid)
        right_merged = self.merge_lists_helper(lists, mid + 1, end)

        # Merge the two halves
        return self.merge_two_lists(left_merged, right_merged)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Divide and Conquer method to merge lists
        return self.merge_lists_helper(lists, 0, len(lists) - 1)