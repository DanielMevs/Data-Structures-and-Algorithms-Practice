from typing import List
from heapq import heappop, heappush


class Solution:
    def minInterval(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        intervals.sort()
        minHeap = []
        result, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heappush(minHeap, (right - left + 1, right))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heappop(minHeap)

            result[q] = minHeap[0][0] if minHeap else -1
        
        return [result[q] for q in queries]