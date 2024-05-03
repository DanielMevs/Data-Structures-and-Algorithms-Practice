from heapq import heappush, heappop


class Solution:
    def maxPerformance(
            self, n: int, speed: list[int],
            efficiency: list[int], k: int
    ) -> int:
        engineers = []
        for eff, spd in zip(efficiency, speed):
            engineers.append([eff, spd])
        engineers.sort(reverse=True)

        result, speed = 0, 0
        minHeap = []
        for eff, spd in engineers:
            if len(minHeap) == k:
                speed -= heappop(minHeap)
            speed += spd
            heappush(minHeap, spd)
            result = max(result, eff * speed)
        
        return result % (10 ** 9 + 7)