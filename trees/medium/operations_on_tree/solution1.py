from collections import deque


class LockingTree:

    def __init__(self, parent: list[int]):
        self.parent = parent
        self.locked = [None] * len(parent)

        self.child = {i: [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True
        
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True
        
    def upgrade(self, num: int, user: int) -> bool:
        i = num
        while i != -1:
            if self.locked[i]:
                return False
            i = self.parent[i]
        
        lockedCount, queue = 0, deque([num])
        while queue:
            n = queue.popleft()
            if self.locked[n]:
                self.locked[n] = None
                lockedCount += 1
            queue.extend(self.child[n])
        if lockedCount > 0:
            self.locked[num] = user

        return lockedCount > 0
        

        


