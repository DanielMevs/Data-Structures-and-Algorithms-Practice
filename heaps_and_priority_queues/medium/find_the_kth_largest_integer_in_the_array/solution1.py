from heapq import heapify, heappop


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        maxHeap = [-int(n) for n in nums]
        heapify(maxHeap)

        while k > 1:
            heappop(maxHeap)
            k -= 1

        return str(-maxHeap[0])