from typing import List
from heapq import heapify, heappop


class Solution:
    def fullBloomFlowers(
            self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i, p in enumerate(people)]
        result = [0] * len(people)
        count = 0
        start = [f[0] for f in flowers]
        end = [f[1] for f in flowers]
        heapify(start)
        heapify(end)
        for p, i in sorted(people):
            while start and start[0] <= p:
                heappop(start)
                count += 1
            while end and end[0] < p:
                heappop(end)
                count -= 1
            result[i] = count

        return result
