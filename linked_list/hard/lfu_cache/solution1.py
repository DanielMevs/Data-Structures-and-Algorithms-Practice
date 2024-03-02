from collections import defaultdict


class ListNode:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)
    
    def popLeft(self):
        result = self.left.next.val
        self.pop(self.left.next.val)
        return result
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCount = 0

        # - Map key -> val
        self.valMap = {}

        # - Map key -> count
        self.countMap = defaultdict(int)

        # - Map count of key -> linkedlist
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        count = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[count].pop(key)
        self.listMap[count + 1].pushRight(key)

        if count == self.lfuCount and not self.listMap[count].length():
            self.lfuCount += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        
        if key not in self.valMap and len(self.valMap) == self.cap:
            result = self.listMap[self.lfuCount].popLeft()
            self.valMap.pop(result)
            self.countMap.pop(result)
        
        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.lfuCount, self.countMap[key])


