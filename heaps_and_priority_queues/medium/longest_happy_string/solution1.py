from heapq import heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heappush(maxHeap, (count, char))
        
        while maxHeap:
            count, char = heappop(maxHeap)
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heappop(maxHeap)
                result += char2
                count2 += 1
                if count2:
                    heappush(maxHeap, (count2, char2))
            else:
                result += char
                count += 1
            if count:
                heappush(maxHeap, (count, char))
        
        return result