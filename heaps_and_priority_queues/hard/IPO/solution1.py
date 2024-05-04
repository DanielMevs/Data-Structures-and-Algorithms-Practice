from heapq import heapify, heappop, heappush


class Solution:
    def findMaximizedCapital(
            self, k: int, w: int,
            profits: list[int], capital: list[int]) -> int:
        maxProfit = []  # only projects we can afford
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapify(minCapital)

        for i in range(k):
            
            while minCapital and minCapital[0][0] <= w:
                c, p = heappop(minCapital)
                heappush(maxProfit, -p)

            if not maxProfit:
                break

            w += -heappop(maxProfit)
        
        return w