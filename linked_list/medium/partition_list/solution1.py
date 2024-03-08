# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(), ListNode()
        leftTail, rightTail = left, right

        while head:
            if head.val < x:
                leftTail.next = head
                leftTail = leftTail.next
            else:
                rightTail.next = head
                rightTail = rightTail.next
            
            head = head.next
        
        leftTail.next = right.next
        rightTail.next = None

        return left.next