class Solution:
    def findCheapestPrice(
            self, n: int, flights: list[list[int]],
            src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            # s = source, d=destination, p=price
            for s, d, p in flights: 
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]