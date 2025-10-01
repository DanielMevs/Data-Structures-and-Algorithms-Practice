from typing import List
import heapq
from math import floor, sqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        def negate(num: int) -> int:
            return -num

        neg_gifts = list(map(negate, gifts))  # negate for max heap
        heapq.heapify(neg_gifts)

        for _ in range(k):
            richest = heapq.heappop(neg_gifts)
            richest_sqrt = floor(sqrt(-richest))  # avoid negative sqrt
            heapq.heappush(neg_gifts, -richest_sqrt)  # negate before pushing

        return sum(list(map(negate, neg_gifts)))
