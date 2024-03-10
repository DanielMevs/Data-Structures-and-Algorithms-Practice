# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
            self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)

        # - Reach node at position "left"
        leftPrev, current = dummy, head
        for i in range(left - 1):
            leftPrev, current = current, current.next

        # - Now current = "left", leftPrev = "node before left"
        # - Reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tempNext = current.next
            current.next = prev
            prev, current = current, tempNext
        
        # - Update pointers
            
        # - Current is the node after "right"
        leftPrev.next.next = current
        # - Prev is "right"
        leftPrev.next = prev

        return dummy.next