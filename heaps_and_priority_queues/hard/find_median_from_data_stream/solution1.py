from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        # - Two heaps, large (minHeap) and small (maxHeap)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)

        # - Make sure every num small is <= every num in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        
        # - Uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # - To account for odd length
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (self.large[0] + (-1 * self.small[0])) / 2
        
