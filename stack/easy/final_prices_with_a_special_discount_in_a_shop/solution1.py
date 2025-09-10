from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [(prices[0], 0)]
        for i in range(1, len(prices)):
            curr = prices[i]
            while stack and stack[-1][0] >= curr:
                val, idx = stack.pop()
                prices[idx] = val - curr
            stack.append((curr, i))
        return prices
