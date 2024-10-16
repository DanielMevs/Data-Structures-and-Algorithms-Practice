from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and head.val > stack[-1]:
                stack.pop()

            stack.append(head.val)
            head = head.next

        head = ListNode()
        curr = head

        for num in stack:
            curr.next = ListNode(num)
            curr = curr.next

        return head.next
