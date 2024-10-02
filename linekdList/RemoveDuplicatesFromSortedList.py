from typing import Optional
import os

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        temp = head
        temp2 = head.next
        last = head.val

        while temp2:
            if temp2.val == last :
                if not temp2.next :
                    temp.next = None
                    break
                temp2 = temp2.next
                temp.next = temp2
            else:
                temp = temp2
                last = temp.val
                temp2 = temp2.next

        return head



