# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        current = head

        for _ in range(k - 1):
            current = current.next

        left = current
        right = head

        while current.next:
            current = current.next
            right = right.next

        left.val, right.val = right.val, left.val

        return head

        