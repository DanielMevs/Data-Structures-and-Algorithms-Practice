from typing import List


class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class LinkedList:
    
    def __init__(self):
        # Dummy node
        self.head = Node(0, None)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        node = self.head.nxt
        result, count = -1, 0
        
        while node:
            if count == index:
                result = node.val
                break
            node, count = node.nxt, count + 1
        
        return result

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head.nxt)
        self.head.nxt = node
        if not node.nxt:
            # If list was empty before inserting
            self.tail = node

    def insertTail(self, val: int) -> None:
        self.tail.nxt = Node(val, None)
        self.tail = self.tail.nxt

    def remove(self, index: int) -> bool:
        curr = self.head
        count = 0

        while count < index and curr:
            curr = curr.nxt
            count += 1
        
        if curr and curr.nxt:
            if curr.nxt == self.tail:
                self.tail = curr
            curr.nxt = curr.nxt.nxt
            return True
        
        return False             
                
    def getValues(self) -> List[int]:
        result = []
        node = self.head.nxt
        while node:
            result.append(node.val)
            node = node.nxt
            
        return result
