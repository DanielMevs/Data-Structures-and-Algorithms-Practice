# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev, current = dummy, head

        while current:
            nxt = current.next

            if current.val == val:
                prev.next = nxt
            else:
                prev = current
            
            current = nxt
        
        return dummy.next