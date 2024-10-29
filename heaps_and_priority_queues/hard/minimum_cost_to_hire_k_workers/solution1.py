from typing import List
from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(
            self, quality: List[int], wage: List[int], k: int) -> float:
        result = float('inf')

        pairs = []  # (ratio, quality)
        for i in range(len(quality)):
            ratio = wage[i] / quality[i]
            pairs.append((ratio, quality[i]))
        pairs.sort(key=lambda pair: pair[0])

        maxHeap = []  # Qualities
        total_quality = 0

        for rate, qual in pairs:
            heappush(maxHeap, -qual)
            total_quality += qual

            if len(maxHeap) > k:
                total_quality += heappop(maxHeap)

            if len(maxHeap) == k:
                result = min(result, rate * total_quality)

        return result
