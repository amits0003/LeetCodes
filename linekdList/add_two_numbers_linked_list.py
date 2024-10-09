"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
from typing import Optional


# l1 = [2, 4, 3]
# l2 = [5, 6, 4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Sol:
    def AddTwoNums(self, s1, s2):
        # res = int("".join(str(item) for item in s1)) + int("".join(str(item) for item in s2))

        head = ListNode(0)
        carry = 0
        current = head

        while s1 is not None or s2 is not None or carry != 0:
            s1val = s1.val if s1 else 0
            s2val = s2.val if s2 else 0

            sum = s1val + s2val + carry

            carry = sum // 10

            current.next = ListNode(sum % 10)

            current = current.next

            s1 = s1.next if s1 else None
            s2 = s2.next if s2 else None

        return head.next


# Create linked lists
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Add two numbers represented by linked lists
obj_sol = Sol()
result = obj_sol.AddTwoNums(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next
