from typing import List
from heapq import heappush, heappop


class Solution:
    def fullBloomFlowers(
            self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i, p in enumerate(people)]
        result = [0] * len(people)

        flowers.sort()
        end = []

        j = 0
        for p, i in sorted(people):
            while j < len(flowers) and flowers[j][0] <= p:
                heappush(end, flowers[j][1])
                j += 1
            while end and end[0] < p:
                heappop(end)
            result[i] = len(end)

        return result
