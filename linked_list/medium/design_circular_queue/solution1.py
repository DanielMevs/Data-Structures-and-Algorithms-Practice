class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        current = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = current
        self.right.prev = current
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val
        
    def isEmpty(self) -> bool:
        return self.left.next == self.right
        
    def isFull(self) -> bool:
        return self.space == 0