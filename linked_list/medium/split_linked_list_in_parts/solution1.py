# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> ListNode:
        length, current = 0, head
        while current:
            current = current.next
            length += 1

        base_len, remainder = length // k, length % k
        current = head
        result = []
        for i in range(k):
            result.append(current)
            for j in range(base_len - 1 + (1 if remainder else 0)):
                if not current:
                    break
                current = current.next
            remainder -= (1 if remainder else 0)
            if current:
                current.next, current = None, current.next

        return result
        