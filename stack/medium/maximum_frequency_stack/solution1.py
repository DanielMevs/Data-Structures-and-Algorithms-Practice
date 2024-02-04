class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxCount = 0
        self.stacks = {}


    def push(self, val: int) -> None:

        valCount = self.count.get(val, 0) + 1
        self.count[val] = valCount

        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stacks[valCount] = []

        self.stacks[valCount].append(val)


    def pop(self) -> int:

        result = self.stacks[self.maxCount].pop()
        self.count[result] -= 1

        if not self.stacks[self.maxCount]:
            self.maxCount -= 1

        return result
        


