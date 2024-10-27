from typing import List
from collections import Counter
from heapq import heapify, heappop


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_count = Counter(arr)
        heap = list(freq_count.values())
        heapify(heap)

        result = len(heap)
        while k > 0 and heap:
            freq = heappop(heap)
            if k >= freq:
                k -= freq
                result -= 1

        return result
