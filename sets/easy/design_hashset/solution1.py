# - Cannot contain duplicate values
# - Handles collisions
class ListNode:
    def __init__(self, key, next=None) -> None:
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        
        current = self.set[key % len(self.set)]

        while current.next:
            # - Stops if duplicate detected
            if current.next.key == key:
                return
            current = current.next
        
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.set[key % len(self.set)]

        while current.next:
            # - Stops if duplicate detected
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        
        

    def contains(self, key: int) -> bool:
        current = self.set[key % len(self.set)]

        while current.next:
            # - Stops if duplicate detected
            if current.next.key == key:
                
                return True
            current = current.next

        return False