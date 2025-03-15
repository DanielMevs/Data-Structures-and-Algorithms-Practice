from typing import List
from sortedcontainers import SortedSet


class SummaryRanges:
    def __init__(self):
        self.sorted_set = SortedSet()

    def addNum(self, value: int) -> None:
        self.sorted_set.add(value)

    def getIntervals(self) -> List[List[int]]:
        result = []

        for n in self.sorted_set:
            if result and result[-1][1] + 1 == n:
                result[-1][1] = n
            else:
                result.append([n, n])

        return result
