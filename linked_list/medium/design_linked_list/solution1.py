class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1

        if current and current != self.right and index == 0:
            return current.val
        
        return -1

        

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and index == 0:
            node, next, prev = ListNode(val), current, current.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and current != self.right and index == 0:
            next, prev = current.next, current.prev
            next.prev = prev
            prev.next = next
            