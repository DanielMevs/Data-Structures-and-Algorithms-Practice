class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        head = self.table[index]

        if not head:
            self.table[index] = Node(key, value)
            
        else:
            prev = None
            while head:
                if head.key == key:
                    head.value = value
                    return
                prev, head = head, head.nxt
            
            prev.nxt = Node(key, value)
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        head = self.table[index]

        while head:
            if head.key == key:
                return head.value
            head = head.nxt
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        head = self.table[index]
        prev = None

        while head:
            if head.key == key:
                if prev:
                    prev.nxt = head.nxt
                else:
                    self.table[index] = head.nxt

                self.size -= 1 
                return True

            prev, head = head, head.nxt
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                index = node.key % self.capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.nxt:
                        new_node = new_node.nxt

                    new_node.nxt = Node(node.key, node.value)
                node = node.nxt
        
        self.table = new_table
