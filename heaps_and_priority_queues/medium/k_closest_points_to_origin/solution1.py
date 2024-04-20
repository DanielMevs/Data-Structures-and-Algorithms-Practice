import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)
        result = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1

        return result
        