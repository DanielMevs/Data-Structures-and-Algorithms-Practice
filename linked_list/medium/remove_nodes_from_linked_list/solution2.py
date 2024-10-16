from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            return prev

        head = reverse(head)
        curr = head
        currentMax = curr.val

        while curr.next:
            if curr.next.val < currentMax:
                curr.next = curr.next.next
            else:
                currentMax = curr.next.val
                curr = curr.next

        return reverse(head)
