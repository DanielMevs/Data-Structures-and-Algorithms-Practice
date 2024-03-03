# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        oldToCopy = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current = current.next
        
        return oldToCopy[head]

        