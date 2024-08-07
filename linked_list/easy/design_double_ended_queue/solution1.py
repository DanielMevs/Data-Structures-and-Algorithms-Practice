class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.nxt == self.tail

    def append(self, value: int) -> None:
        node = Node(value)
        last_node = self.tail.prev

        last_node.nxt = node
        node.prev = last_node
        node.nxt = self.tail
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        first_node = self.head.nxt

        first_node.prev = node
        node.nxt = first_node
        node.prev = self.head
        self.head.nxt = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last_node = self.tail.prev
        val = last_node.val
        prev_node = last_node.prev

        prev_node.nxt = self.tail
        self.tail.prev = prev_node

        return val
    
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        first_node = self.head.nxt
        val = first_node.val
        next_node = first_node.nxt

        next_node.prev = self.head
        self.head.nxt = next_node

        return val
