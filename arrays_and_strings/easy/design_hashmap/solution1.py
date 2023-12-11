class ListNode:
    def __init__(self, key=-1, val=1, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        current = self.map[index]
        while current.next:
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        current = self.map[index].next
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1
        
    def remove(self, key: int) -> None:
        index = self.hash(key)
        current = self.map[index]
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next