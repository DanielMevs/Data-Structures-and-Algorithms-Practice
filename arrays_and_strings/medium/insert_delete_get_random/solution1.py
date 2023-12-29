from random import choice

class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        result = val not in self.numMap

        if result:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)

        return result

    def remove(self, val: int) -> bool:
        result = val in self.numMap

        if result:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]

        return result

    def getRandom(self) -> int:
        return choice(self.numList)