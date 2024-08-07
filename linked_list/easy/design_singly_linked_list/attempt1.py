from typing import List


class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class LinkedList:
    
    def __init__(self):
        self.root = Node(0, None)
    
    def get(self, index: int) -> int:
        node = self.root
        result, count = -1, 0
        
        while node:
            if count == index:
                result = node.val
                break
            node, count = node.nxt, count + 1
        
        return result

    def insertHead(self, val: int) -> None:
        node = Node(val, self.root)
        self.root = node

    def insertTail(self, val: int) -> None:
        node = self.root

        while node.nxt:
            node = node.nxt
        
        new_node = Node(val, None)
        node.nxt = new_node

    def remove(self, index: int) -> bool:
        prev = Node(0, self.root)
        temp = prev
        curr = self.root
        count = 0

        while curr:
            if index == count:
                prev.nxt = curr.nxt
                curr.nxt = None
                break
            prev = curr
            curr = curr.nxt
            count += 1
        
        self.root = temp.nxt
        return count == index                
                
    def getValues(self) -> List[int]:
        result = []
        node = self.root
        while node:
            result.append(node.val)
            node = node.nxt
        return result
