# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, current = head, head.next

        while current:
            if current.val >= prev.val:
                prev, current = current, current.next
                continue
            
            temp = dummy
            while current.val > temp.next.val:
                temp = temp.next

            prev.next = current.next
            current.next = temp.next
            temp.next = current
            current = prev.next

        return dummy.next