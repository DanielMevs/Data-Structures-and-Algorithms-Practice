class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def isEmpty(self) -> bool:
        return not self.head.nxt

    def append(self, value: int) -> None:
        self.tail.nxt = Node(value, None, self.tail)
        self.tail = self.tail.nxt

    def appendleft(self, value: int) -> None:
        self.head.nxt = Node(value, self.head.nxt, self.head)

    def pop(self) -> int:
        val = self.tail.val
        self.tail.prev.nxt = None
        self.tail = self.tail.prev
        
        return val
    
    def popleft(self) -> int:
        
        if not self.isEmpty():
            val = self.head.nxt.val
            self.head.nxt = self.head.nxt.nxt
            self.head.nxt.prev = self.head
        else:
            val = self.head.val

        return val
