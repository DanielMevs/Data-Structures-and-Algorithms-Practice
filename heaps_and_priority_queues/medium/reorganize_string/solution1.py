from heapq import heapify, heappop, heappush
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapify(maxHeap)  # O(n)

        prev = None
        result = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            # - Most frequent, except prev
            cnt, char = heappop(maxHeap)
            result += char
            cnt += 1

            if prev:
                heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        
        return result