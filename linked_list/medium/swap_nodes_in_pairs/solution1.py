# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current and current.next:
            # - Save pointers
            nextPair = current.next.next
            second = current.next

            # - Reverse this pair
            second.next = current
            current.next = nextPair
            prev.next = second

            # - Update pointers
            prev = current
            current = nextPair
        
        return dummy.next